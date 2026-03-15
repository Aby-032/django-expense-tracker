from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm
from django.http import HttpResponse

# Create your views here.

# Home Page
def home(request):
    return HttpResponse("!!! HOME PAGE UNDER CONSTRUCTION !!!")

# Expense List
def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, "expenses/expense_list.html", {"expenses": expenses})

# Add Expense
def add_expense(request):

    if request.method == "POST":
        form = ExpenseForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("expense_list")

    else:
        form = ExpenseForm()

    return render(request, "expenses/add_expense.html", {"form": form})