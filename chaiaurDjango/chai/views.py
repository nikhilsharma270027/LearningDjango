from django.shortcuts import render

# Create your views here.
def all_chai(request):
    chai_list = [
        {"name": "Masala Chai", "description": "A spicy tea with a blend of aromatic spices."},
        {"name": "Green Chai", "description": "A healthy tea made with green tea leaves."},
        {"name": "Ginger Chai", "description": "A soothing tea infused with fresh ginger."},
    ]
    return render(request, 'chai/all_chai.html', {'chai_list': chai_list})