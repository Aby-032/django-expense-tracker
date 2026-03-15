from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required 
from .models import Expense
from .forms import ExpenseForm

# Create your views here.

# Home Page
def home(request):
    return HttpResponse("!!! HOME PAGE UNDER CONSTRUCTION !!!")

# Expense List
@login_required
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)
    return render(request, "expenses/expense_list.html", {"expenses": expenses})

# Add Expense
@login_required
def add_expense(request):

    if request.method == "POST":
        form = ExpenseForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("expense_list")

    else:
        form = ExpenseForm()

    return render(request, "expenses/add_expense.html", {"form": form})