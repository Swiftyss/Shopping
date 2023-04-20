from .models import * 

def cartcount(request):
    reading = Shopcart.objects.filter(user__username=request.user.username, paid=False)
    cartcount = 0
    for item in reading:
        cartcount += item.quantity 

    context = {
        'cartcount': cartcount,
    }
    return context
