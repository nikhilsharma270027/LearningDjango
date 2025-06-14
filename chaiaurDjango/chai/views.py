from django.shortcuts import render
from .models import ChaiVarity, Store  # Ensure the model is imported correctly
from django.shortcuts import get_object_or_404 # get object or 404 is used to fetch a single object or return a 404 error if not found
from .forms import ChaiVarietyForm  # Import the form for chai variety selection

# Create your views here.
def all_chai(request):
    chais = ChaiVarity.objects.all()  # Fetch all chai varieties from the database
    return render(request, 'chai/all_chai.html', {'chais': chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVarity, pk=chai_id)
    return render(request, 'chai/chai_details.html', {'chai': chai})

def chai_store_view(request):
    stores = None
    if request.method == 'POST':
        form = ChaiVarietyForm(request.POST)
        if form.is_valid():
            chai_variety = form.cleaned_data['chai_variety'] # inside [] is used to access the value of the field its in forms file variable name
            stores = Store.objects.filter(chai_varity=chai_variety)  # Fetch stores that sell the selected chai variety
        else:
            form = ChaiVarietyForm()
    return render(request, 'chai/chai_stores.html', {'stores': stores})