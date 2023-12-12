#customer_wise_sales_report.py
from django.shortcuts import render
import pandas as pd
from datetime import datetime
import pytz
from restaurant_app.models import Invoicemain, Customermaster, Invoicesub
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
import numpy as np

# Create your views here.
@csrf_exempt
@login_required
def customer_wise_sales_report(request):
    json_data = []
    total_net = 0
    total_vat = 0
    total_discount = 0
    grand_total = 0

    if request.method=="POST":
        start_date_str = request.POST.get('start_date')
        end_date_str = request.POST.get('end_date')

        if start_date_str is not None and end_date_str is not None:
            start_date = pytz.utc.localize(datetime.strptime(start_date_str,'%Y-%m-%d'))
            end_date = pytz.utc.localize(datetime.strptime(end_date_str,'%Y-%m-%d'))
            date_ranges = [(start_date, end_date)]

            aggregated_data = [
                {
                    'Invoice_Date': rec.invdate,
                    'Customer_ID': cm.custid,
                    'Customer_Name': cm.custname,
                    'Total_Net': rec.totamt,
                    'Total_Vat': rec.vatamount,
                    'DISC': item.discamt
                }
                for from_date, to_date in date_ranges
                for rec in Invoicemain.objects.filter(invdate__gte=from_date, invdate__lte=to_date, cancelstatus=0)
                for item in Invoicesub.objects.filter(itemid=rec.invid)
                for cm in Customermaster.objects.filter(custid=rec.custid)
            ]
            try:
                df = pd.DataFrame(aggregated_data)
                if 'Invoice_Date' in df.columns:
                    df['Invoice_Date'] = pd.to_datetime(df['Invoice_Date'])
                    df = df.sort_values('Invoice_Date', ascending=True)

                    filtered_data = df[(df['Invoice_Date'] >= start_date) & (df['Invoice_Date'] <= end_date)]
                    filtered_data['Total_Vat'] = filtered_data['Total_Vat'].round(2)
                    filtered_data['Grand_Total'] = filtered_data['Total_Net'] + filtered_data['Total_Vat']
                    filtered_data['Invoice_Date'] = filtered_data['Invoice_Date'].dt.strftime('%Y-%m-%d')

                    total_net = np.round(filtered_data['Total_Vat'].sum(),2)
                    total_vat = np.round(filtered_data['Total_Vat'].sum(),2)
                    grand_total = np.round(filtered_data['Grand_Total'].sum(),2)
                    total_discount = np.round(filtered_data['DISC'].sum(),2)
                    print(filtered_data)
                    json_records = filtered_data.reset_index().to_json(orient='records', date_format='iso')
                    json_data = json.loads(json_records)
                    return JsonResponse(json_data, safe=False)
                else:
                    pass
            except Exception as ex:
                print("---------------- Error ----------------", str(ex))
                return JsonResponse({'error': str(ex)}, status=500)               
    return render(request, 'customer_wise_sales_report.html', {'filtered_data': json_data,'Total_Net':total_net,
                                                               'Total_VAT':total_vat,'Grand_Total':grand_total,
                                                               'Total_Discount':total_discount})