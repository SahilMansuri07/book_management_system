from django.shortcuts import render
from django import http
from .models import Author,Book,Registration
from .forms import AuthorRegistration,BookRegistration,UserRegistration,loginchecking

# Create your views here.
def registration(request):
    if request.method == 'POST':
        fm = UserRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            cpass = request.POST['cpass']
            if cpass != password:
                return http.HttpResponse("Confirm password is same as Pasword.")
            register = Registration(name=name,email=email,password=password)
            register.save()
            return http.HttpResponseRedirect('/management/login')
    fm = UserRegistration()
    return render(request,'registration.html',{'fm':fm})


def login(request):
    if request.method == 'POST':
        fm = loginchecking(request.POST)
        if fm.is_valid():
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            try:
                user = Registration.objects.get(email=email,password=password)
                request.session['s_name'] = user.name
                response = http.HttpResponseRedirect('/management/admin')
                response.set_cookie('c_name',user.name)
                return response
            except Registration.DoesNotExist:
                return http.HttpResponse("Wrong Email or password entered.")
    fm = loginchecking()
    return render(request,'login.html',{'fm':fm})


def admin(request):
    s_name = request.session.get('s_name')
    c_name = request.COOKIES.get('c_name')
    if s_name is None and c_name is None:
        return http.HttpResponseRedirect('/management/login')
    elif request.method == 'POST':
        fm = AuthorRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            address = fm.cleaned_data['address']
            au = Author(name=name,address=address)
            au.save()
            return http.HttpResponseRedirect('/management/admin')
    fm = AuthorRegistration()
    return render(request,'admin.html',{'name':c_name,'fm':fm})


def logout(request):
    del request.session['s_name']
    response = http.HttpResponseRedirect('/management/login')
    response.delete_cookie('c_name')
    return response


def home(request):
    s_name = request.session.get('s_name')
    c_name = request.COOKIES.get('c_name')
    if s_name is None and c_name is None:
        return http.HttpResponseRedirect('/management/login')
    elif request.method == 'POST':
        fm = BookRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            isbn = fm.cleaned_data['isbn']
            price = fm.cleaned_data['price']
            author = request.POST['author']
            auid = Author.objects.get(id=author)
            bk = Book(name=name,isbn=isbn,price=price,author=auid)
            bk.save()
            return http.HttpResponseRedirect('/management/home')
    au = Author.objects.all()
    book = Book.objects.all()
    fm = BookRegistration()
    return render(request,'home.html',{'fm':fm,'book':book,'au':au,'name':c_name})


def update(request,id):
    if request.method == 'POST':
        fm = BookRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            isbn = fm.cleaned_data['isbn']
            price = fm.cleaned_data['price']
            author = request.POST['author']
            auid = Author.objects.get(id=author)
            bkid = request.POST['bkid']
            bk = Book.objects.get(id=bkid)
            bk.name = name
            bk.isbn = isbn
            bk.price = price
            bk.author = auid
            bk.save()
            return http.HttpResponseRedirect('/management/home')
    pi = Book.objects.get(pk=id)
    fm = BookRegistration(instance=pi)
    au = Author.objects.all()
    return render(request,'update.html',{'fm':fm,'bkid':id,'au':au})


def delete(request,id):
    pi = Book.objects.get(pk=id)
    pi.delete()
    return http.HttpResponseRedirect('/management/home')