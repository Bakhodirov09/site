from django.shortcuts import render

def view_portfolio(request):
    data = request.GET
    num1 = int(data.get("num1", 0))
    num2 = int(data.get("num2", 0))
    amal = data.get("amal", "+")
    result = None
    if amal == "+":
        result = num1 + num2
    elif amal == "-":
        result = num1 - num2
    elif amal == "*":
        result = num1 * num2
    elif amal == "/":
        result = num1 / num2
    else:
        result = "Kechirasiz + - * / Amallaridan Birini Kiriting!"
    context = {
        "result": result
    }
    return render(request, 'games.html', context)