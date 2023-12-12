from django.urls import path
from restaurant_app.views import user_login, create_account, forget_password, logout
from django.contrib.auth import views as auth_views

from restaurant_app.VAT_sales_report import vat_sales_report
from restaurant_app.customer_wise_sales_report import customer_wise_sales_report
from restaurant_app.category_wise_sales_report import category_wise_sales_report
from restaurant_app.item_wise_sales_report import item_wise_sales_report
from restaurant_app.sales_report import sales_report

urlpatterns = [
    #### Account Login ####
    path('login/', user_login, name='login'),

    #### Account Logout ####
    path('logout/', logout, name='logout'),

    #### Create Account ####
    path('create_account/', create_account, name='create_account'),

    #### ForgetPassword ####
    path('forget_password/', forget_password, name='forget_password'),

    #### PasswordReset ####
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    #### Report ####
    path('sales_report/', sales_report, name='sales_report'),
    path('vat_sales_report/', vat_sales_report, name='vat_sales_report'),
    path('customer_wise_sales_report/', customer_wise_sales_report, name='customer_wise_sales_report'),
    path('item_wise_sales_report/', item_wise_sales_report, name='item_wise_sales_report'),
    path('category_wise_sales_report/', category_wise_sales_report, name='category_wise_sales_report'),
]