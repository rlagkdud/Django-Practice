from django.shortcuts import render

# Create your views here.
def board(request):
    return render(request,'board.html')

def boardfirst(req):
    return render(req, 'boardfirst.html')