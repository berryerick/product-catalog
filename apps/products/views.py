from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'products/index.html')
def product(request, product_id):
	product = {}
	context = {
		'product': product
	}
	return render(request, 'products/product.html')