from django.shortcuts import render
from .models import customer
# Create your views here.
def index(request):
    top_deals = customer.objects.all()
    return render(request, 'index.html', {'top_deals': top_deals})