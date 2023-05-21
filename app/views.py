from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from app import utils
from app import models

# Variable to track state of Cart
CART = {}

def index(request):
    return render(request, 'index.html')

def tools(request):
    if request.session.get('logged_in'):
        context = {}
        medicine = request.GET.get('medicine')
        country = request.GET.get('country')
        if medicine and country:
            sale_prediction = utils.predict(medicine, country)
            context = {'predict': sale_prediction}
            return render(request, 'results.html', context)
        elif medicine:
            context = {'variables': utils.variables, 'countrys': utils.get_countrys(medicine)}
            return render(request, 'tools.html', context)
        context = {'variables': utils.variables }
        return render(request, 'tools.html', context)
    return redirect('/')

def about_us(request):
    return render(request, 'aboutus.html')

def log_in(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(username=email)
        if user.exists():
            user = User.objects.get(username=email)
            if user.check_password(password):
                request.session['logged_in'] = True
                return redirect('/')
            else:
                context = {'msg': 'Invalid email or password'}
                return render(request, 'auth/login.html', context)
        else:
            context = {'msg': 'Account does not exist!'}
            return render(request, 'auth/login.html', context)
    return render(request, 'auth/login.html')

def sign_up(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(username=email)
        if user.exists():
            context = {'msg': 'Account Already Registered! Please Login'}
            return render(request, 'auth/signup.html', context)
        user = User(username=email)
        user.set_password(password)
        user.save()
        request.session['logged_in'] = True
        return redirect('/')
    return render(request, 'auth/signup.html')

def log_out(request):
    if request.session.get('logged_in'):
        request.session.pop('logged_in')
        return redirect('/')
    return redirect('/login/')

def shop(request):
    context = {}
    if request.method == "POST":
        med = request.POST.get("med")
        medId = request.POST.get("medId")
        medPrice = request.POST.get("medPrice")
        medUnitsQty = request.POST.get("unitQty")
        if request.POST.get('action') == "add":
            CART[med] = {
                'qty': 1,
                'name': med,
                'id': medId,
                'price': medPrice,
                'units': medUnitsQty
            }
        elif request.POST.get('action') == "delete":
            if CART.get(med) != None:
                CART.pop(med)
    med = request.GET.get('q')
    if med:
        medicines = models.Medicine.objects.filter(name__icontains=med)
    else:
        medicines = models.Medicine.objects.all()
    context['CART'] = CART
    context['medicines'] = medicines
    # print(CART)
    return render(request, 'shop/shop.html', context)

def fill_stock(request, med_id):
    context = {}
    if request.method == "POST":
        msg="Order Sent Successfully!"
        return redirect(f'/shop/?msg={msg}')
    med = models.Medicine.objects.get(pk=med_id)
    context['med'] = med
    return render(request, 'shop/fillstock.html', context)

def cart_view(request):
    context = {}
    context['CART'] = CART
    if request.method == "POST":
        total = 0
        for i in CART:
            qty = request.POST.get(i)
            CART[i]['qty'] = qty
            total += (int(qty) * int(CART[i]['price']))
            med = models.Medicine.objects.get(id=CART[i]['id'])
            med.units -= int(qty)
            med.save()
        context['total'] = total
        CART.clear()
        return render(request, 'shop/bill.html', context)        
    return render(request, 'shop/cart.html', context)