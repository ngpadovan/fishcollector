from django.shortcuts import render

fishes = [
  {'name': 'Swimmy', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
  {'name': 'Scaley', 'breed': 'calico', 'description': 'gentle and loving', 'age': 0},
]

# Create your views here.

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def fishes_index(request):
    return render(request, 'fishes/index.html', {
        'fishes': fishes

})