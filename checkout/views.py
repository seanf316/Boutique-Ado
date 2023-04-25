from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get("bag", {})
    if not bag:
        messages.error(request, "Theres nothing in your bag at the moment")
        return redirect(reverse("products"))

    order_form = OrderForm()
    template = "checkout/checkout.html"
    context = {
        "order_form": order_form,
        "stripe_public_key": "pk_test_51N0ucVJ2Zqv7CR6ur2j8RGhR537KAAMs1CCbmLroY87VpORKCunhsKdKgTUBOzQibOlfhTUJPwpZIwxUD0nGPHOw00iZD6JZTk",
        "client_secret": "test client secret",
    }

    return render(request, template, context)
