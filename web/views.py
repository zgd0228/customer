import re
from django.shortcuts import render,HttpResponse,redirect
from rbac.models import *
from web.models import *
from rbac.Middlewares.permission_session import *
# Create your views here.
def login(request):
    if request.method == 'POST':
        name = request.POST.get('user')
        pwd = request.POST.get('pwd')
        user = UserInfo.objects.filter(name=name,pwd=pwd).first()
        if user:
            init_session(request,user)
            return redirect('/customer/list/')
        else:
            return HttpResponse('用户名或密码错误')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('user')
        pwd = request.POST.get('pwd')
        tel = request.POST.get('tel')
        email = request.POST.get('email')
        age = request.POST.get('age')
        user = UserInfo.objects.filter(name=name).first()
        if user:
            return HttpResponse('用户已存在')
        else:
            UserInfo.objects.create(name=name,age=age,tel=tel,pwd = pwd, email=email)

    return render(request,'register.html')

def customer_list(request):

    user_list = Customer.objects.all()


    return render(request, 'customer_list.html', locals())

def customer_add(request):
    if request.method == "POST":
        user = request.POST.get('user')
        tel = request.POST.get('tel')
        email = request.POST.get('email')
        age = request.POST.get('age')
        Customer.objects.create(name = user,age = age,tel = tel,email = email)
        redirect('/customer/list/')
    return render(request, 'customer_add.html')

def customer_delete(request,id):

    return redirect('/customer/list/')

def customer_edit(request,id):

    return render(request, 'customer_edit.html', locals())

def payment_list(request):

    pay_list = Payment.objects.all()

    return render(request, 'pay_list.html', locals())

def payment_add(request):

    user_list = Customer.objects.all()
    if request.method == 'POST':
        user = request.POST.get('user')
        money = request.POST.get('money')
        print(user,money)
        # user_id = Customer.objects.filter(name=user).first().id
        # Payment.objects.create(money = money,customer_id = user_id)
        # redirect('/pay/list/')
    return render(request, 'pay_add.html', locals())

def pay_delete(request,id):

    return redirect('/pay/list/')

def pay_edit(request,id):

    return render(request, 'pay_edit.html', locals())