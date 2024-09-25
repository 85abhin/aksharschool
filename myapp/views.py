from django.shortcuts import render, redirect, HttpResponse
from .forms import StudentRegistrationForm, StudentFeesform
from django.contrib import messages
from .models import StudentRegistration, StudentFees, FeesAmount
from django.utils import timezone
from .paytm import generate_checksum, verify_checksum
import time
from aksharschool import settings
# Create your views here.

def base(request):
    return render(request,"myapp/base.html")

def home(request):
    return render(request,"myapp/home.html")

def pay_fees(request,identifier):
    stud_data = StudentRegistration.objects.get(mobile_number=identifier)
    print(stud_data.first_name)
    print(stud_data.last_name)
    print(stud_data.email)
    fees = 750
    context = {
        'first_name': stud_data.first_name,
        'last_name': stud_data.last_name,
        'email': stud_data.email,
        'fees': fees
    }
    return render(request, 'myapp/fees2.html', context)

def pay_fees_view(request):
    if request.method == 'POST':
        identifier = request.POST.get('identifier')
        message = pay_fees(request,identifier)
        return HttpResponse(message)
    return render(request, 'myapp/fees1.html')


def process_payment(request):
    if request.method == 'POST':
        identifier = request.POST.get('identifier')
        # Here, you would redirect to the actual payment portal.
        # For simulation, we redirect directly to the success page.
        return redirect('payment_success')
    return redirect('home')


def payment_success(request):
    return render(request, 'myapp/success.html')


# This is a for student registration
def studentregistraionform(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student registered successfully.')
            return redirect('studentreg')  # Redirect to a success page or another view
    else:
        form = StudentRegistrationForm()
    return render(request, 'myapp/registration.html', {'form': form})


# ------------------------------------------------
def payment_success(request):
    return render(request, 'myapp/success.html')

def payment_failure(request):
    return render(request, 'myapp/failure.html')

def downloads(request):
    return render(request,"myapp/downloads.html")

def studentfees(request):
    return render(request,"myapp/fees1.html")

def studentresult(request):
    return render(request,"myapp/result.html")

def payment_cancel(request):
    return render(request, 'myapp/cancel.html')



