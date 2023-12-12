import json
from django.shortcuts import render
import pandas as pd
from datetime import datetime
import pytz
from restaurant_app.models import Invoicemain, Invoicesub, Itemmaster, Subgroupmaster
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.
@csrf_exempt
@login_required
def category_wise_sales_report(request):
    json_data = []
    total_quantity = 0
    total_disc = 0
    total_amount = 0
    total_price = 0

    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        if start_date is not None and end_date is not None:
            start_date = pytz.utc.localize(datetime.strptime(start_date, '%Y-%m-%d'))
            end_date = pytz.utc.localize(datetime.strptime(end_date, '%Y-%m-%d'))

            date_ranges = [(start_date, end_date)]

            aggregated_data = [
                {
                    'Category_ID': im.subgroupid,
                    'Category_Name': Subgroupmaster.objects.get(subgroupid=im.subgroupid).subgroupname,
                    'Invoice_Date': rec.invdate,
                    'Item_ID': item.itemid,
                    'Item_Name': im.itemname,
                    'Quantity': item.qty,
                    'Selling_Price': im.sellingprice,  # Define Selling_Price
                    'DISC': item.discamt,
                    'TotalAmount': (item.qty) * (im.sellingprice)  # Define TotalAmount
                }
                for from_date, to_date in date_ranges
                for rec in Invoicemain.objects.filter(invdate__gte=from_date, invdate__lte=to_date, cancelstatus=0).order_by('invdate')
                for item in Invoicesub.objects.filter(invid=rec.invid, status=0).order_by('invid')
                for im in Itemmaster.objects.filter(itemid=item.itemid)
            ]

            df = pd.DataFrame(aggregated_data)
            df['Invoice_Date'] = pd.to_datetime(df['Invoice_Date'], format='%Y-%m-%d', errors='coerce')

            if 'Invoice_Date' in df.columns:
                df['Invoice_Date'] = pd.to_datetime(df['Invoice_Date'])
                df = df.sort_values('Invoice_Date', ascending=True)
                df = df.sort_values('Category_ID', ascending=True)

                filtered_data = df[(df['Invoice_Date'] >= start_date) & (df['Invoice_Date'] <= end_date)]
                filtered_data['Quantity'] = filtered_data['Quantity'].astype(float)
                filtered_data['Quantity'] = filtered_data['Quantity'].round(2)
                filtered_data['Selling_Price'] = filtered_data['Selling_Price'].astype(float)
                filtered_data['DISC'] = filtered_data['DISC'].astype(float)
                filtered_data['DISC'] = filtered_data['DISC'].round(2)
                filtered_data['TotalAmount'] = filtered_data['TotalAmount'].astype(float)
                filtered_data['TotalAmount'] = filtered_data['TotalAmount'].round(2)
                
                print(filtered_data)
                total_amount = filtered_data['TotalAmount'].sum()
                total_quantity = filtered_data['Quantity'].sum()
                total_disc = filtered_data['DISC'].sum()
                total_price = filtered_data['Selling_Price'].sum()
                
                print("---------------- Totals ------------- ", total_quantity, total_price, total_disc, total_price, sep='\n')
                json_records = filtered_data.reset_index().to_json(orient='records', date_format='iso')
                json_data = json.loads(json_records)

                return JsonResponse(json_data, safe=False)
    return render(request, 'category_wise_sales_report.html', {'filtered_data': json_data, 'Total_Quantity':total_quantity,
                                                               'Total_DISC': total_disc, 'Total_Price':total_price,
                                                               'TotalAmount':total_amount})
