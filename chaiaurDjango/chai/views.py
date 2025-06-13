from django.shortcuts import render
from .models import ChaiVarity  # Ensure the model is imported correctly
from django.shortcuts import get_object_or_404 # get object or 404 is used to fetch a single object or return a 404 error if not found
# Create your views here.
def all_chai(request):
    chais = ChaiVarity.objects.all()  # Fetch all chai varieties from the database
    return render(request, 'chai/all_chai.html', {'chais': chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVarity, pk=chai_id)
    return render(request, 'chai/chai_details.html', {'chai': chai})