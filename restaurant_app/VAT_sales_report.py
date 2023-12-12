from django.shortcuts import render
import pandas as pd
from datetime import datetime
import pytz
from restaurant_app.models import Invoicemain
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
import numpy as np

@csrf_exempt
@login_required
def vat_sales_report(request):
    json_data = []
    total_amount = 0
    item_discount = 0
    invoice_discount = 0
    before_vat = 0
    after_vat = 0
    five_percent_Vat_amount = 0

    if request.method == "POST":
        start_date_str = request.POST.get('start_date')
        end_date_str = request.POST.get('end_date')

        if start_date_str is not None and end_date_str is not None:
            start_date = pytz.utc.localize(datetime.strptime(start_date_str, '%Y-%m-%d'))
            end_date = pytz.utc.localize(datetime.strptime(end_date_str, '%Y-%m-%d'))
            date_ranges = [(start_date, end_date)]

            aggregated_data = [
                {
                    'Invoice_Date': rec.invdate,
                    'Invoice_Number': rec.invid,
                    'TotalAmount': rec.totamt,
                    'ItemDiscount': rec.itemdiscamt,
                    'InvoiceDiscount': rec.invoicediscamt,
                    'Before_Vat': rec.grandtotal,
                    'five_percent_Vat_Amount': rec.vatamount,
                    'After_Vat': rec.totamt
                }
                for from_date, to_date in date_ranges
                for rec in Invoicemain.objects.filter(invdate__gte=from_date, invdate__lte=to_date, cancelstatus=0)
            ]

            df = pd.DataFrame(aggregated_data)
            df['Invoice_Date'] = pd.to_datetime(df['Invoice_Date'], format='%Y-%m-%d', errors='coerce')
            df['Before_Vat'] = df['Before_Vat'].round(2)
            df['five_percent_Vat_Amount'] = df['five_percent_Vat_Amount'].round(2)
            df['After_Vat'] = df['After_Vat'].round(2)
            print("------ Column Names ------", df.columns, sep='\n')

            if 'Invoice_Date' in df.columns:
                df['Invoice_Date'] = pd.to_datetime(df['Invoice_Date'])
                df = df.sort_values('Invoice_Date', ascending=True)

                filtered_data = df[(df['Invoice_Date'] >= start_date) & (df['Invoice_Date'] <= end_date)]
                filtered_data['Invoice_Date'] = filtered_data['Invoice_Date'].dt.strftime('%d-%m-%Y')
                filtered_data['five_percent_Vat_Amount'] = np.round(filtered_data['five_percent_Vat_Amount'], 2)
                filtered_data['After_Vat'] = np.round(filtered_data['After_Vat'], 2)
                filtered_data['Before_Vat'] = np.round(filtered_data['Before_Vat'], 2)
                
                total_amount = filtered_data['TotalAmount'].sum()
                item_discount = filtered_data['ItemDiscount'].sum()
                invoice_discount = filtered_data['InvoiceDiscount'].sum()
                before_vat = np.round(filtered_data['Before_Vat'].sum(), 2)
                five_percent_Vat_amount = np.round(filtered_data['five_percent_Vat_Amount'].sum(), 2)
                after_vat = np.round(filtered_data['After_Vat'].sum(), 2)

                print(filtered_data)
                print("------------------- Totals -------------------")
                print(total_amount,item_discount,invoice_discount,before_vat,five_percent_Vat_amount,after_vat,sep='\n')

                json_records = filtered_data.reset_index().to_json(orient='records', date_format='iso')
                json_data = json.loads(json_records)
                return JsonResponse(json_data, safe=False)
    return HttpResponse(render(request, 'vat_sales_report.html', {'filtered_data': json_data, 'TotalAmount':total_amount,
                                                                  'ItemDiscount':item_discount,'InvoiceDiscount':invoice_discount,
                                                                  'BeforeVat':before_vat,'Five_Percent_VAT_Amount':five_percent_Vat_amount,
                                                                  'AfterVat':after_vat}))