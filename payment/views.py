from .models import Product,Order
from django.urls import reverse
from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm



def home(request):
    product=Product.objects.all()
    paypal_dict = {
        "business": "sb-0xfml26186671@business.example.com",
        "amount": "10",
        "item_name": "iphone",
        "invoice": "unique-invoice-id",
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "return": request.build_absolute_uri(reverse('successful_view')),
        "cancel_return": request.build_absolute_uri(reverse('cancelled_view')),
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render(request, "home.html", context)


def successful_view(request):
    return render(request,'successful.html')

def cancelled_view(request):
    return  render(request,'cancelled.html')

