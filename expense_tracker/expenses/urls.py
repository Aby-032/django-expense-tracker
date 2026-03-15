from django.urls import path
from .views import home, expense_list, add_expense

urlpatterns = [
    path('', home, name="home"),
    path('list/', expense_list, name="expense_list"),
    path('add/', add_expense, name="add_expense"),
]