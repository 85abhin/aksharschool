
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='homepage'),
    path('base/',views.base),
    path('studentregistraion/',views.studentregistraionform,name="studentreg"),
    path('downloads/',views.downloads,name="downloadspage"),
    path('fees/',views.studentfees,name="feespage"),
    path('pay-fees/', views.pay_fees_view, name='pay_fees'),
    path('result/',views.studentresult,name="resultpage"),
    path('process-payment/', views.process_payment, name='process_payment'),
    path('payment-success/', views.payment_success, name='payment_success'),
    path('payment-cancel/', views.payment_cancel, name='payment_cancel'),
    
    
]
