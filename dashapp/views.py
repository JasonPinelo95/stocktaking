from django.shortcuts import render
from .models import *
from .filters import StocktakingFilter
from django.contrib.auth.decorators import login_required
# from .forms import 

# Create your views here.
# Vista del menu dashboard de la App Log in (reuiqeres estar logueado para acceder)
@login_required
def dashboardView(request):
    return render(request,'dash.html')
# url = http://localhost:8000/dashapp/dash/