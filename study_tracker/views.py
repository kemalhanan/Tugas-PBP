from django.shortcuts import render

# Create your views here.
def show_tracker(request):
    return render(request, "tracker.html")