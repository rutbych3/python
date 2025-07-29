from django.shortcuts import render

# Create your views here.
def menu_view_test(request):
    return render(request, "menu_app/menu.html")