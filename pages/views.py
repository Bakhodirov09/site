from django.shortcuts import render

def view_portfolio(request):
    return render(request, 'games.html')