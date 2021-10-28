from typing import Type
from django import http
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import *

# Create your views here.


def home(request):
    fields = Book._meta.fields
    data = Book.objects.filter(is_active=True)
    return render(request, "bookstore/home.html", locals())


def edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # new_price = request.POST['price']
    # new_market_price = request.POST['market-price']
    # book.price =
    return render(request, "bookstore/edit.html", locals())


def submit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    delete = request.POST.get("delete-record", False)
    if delete:
        return HttpResponseRedirect(reverse("bookstore:home"))
    try:
        new_price = request.POST["price"]
        new_market_price = request.POST["market-price"]

        # print(delete)
        # return HttpResponseRedirect(reverse("bookstore:home"))
        if new_price or new_market_price:
            if new_price:
                if not new_price.isdigit():
                    raise TypeError
                else:
                    book.price = float(new_price)
                    book.save()
            if new_market_price:
                if not new_market_price.isdigit():
                    raise TypeError
                else:
                    book.market_price = float(new_market_price)
                    book.save()
        else:
            print("both empty")
            raise ValueError

    except (ValueError, TypeError):
        # error_message = ""
        # if ValueError:
        #     error_message += "empty values entered"
        # if TypeError:
        #     error_message += "entry must be integer"
        return render(
            request,
            "bookstore/edit.html",
            {
                "book": book,
                "error_message": "error please resubmit",
            },
        )
    return HttpResponseRedirect(reverse("bookstore:home"))
