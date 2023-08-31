from django.shortcuts import render
from .models import Collage
# Create your views here.
def collage(request):
    collagee = Collage.objects.all()
    return render(request, "collage.html", {'collagee':collagee})