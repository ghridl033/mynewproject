from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import Members
# Create your views here.

def login_after(req):
    user_name = req.session.get('user')

    if user_name:
        return render(req, "loginafter.html", {'message': user_name} )
    return redirect("/")

def logout(req):
    if req.session.get('user'):
        del(req.session['user'])

    return redirect("/")

def login(req):
    if req.method == 'GET':
        return render(req, 'login.html')
    elif req.method == 'POST':
        useremail = req.POST.get('useremail', None)
        password = req.POST.get('password', None)
        
        err = {}
        if not (useremail and password) :
            err['err'] = '유효성이 잘못되었습니다.'
            return render(req, 'login.html', err)
        else:
            member = Members.objects.get(useremail=useremail)
            

            if password == member.password :
                req.session['user'] = member.username
                return redirect('/members')
            else:
                err['err'] = "비밀번호가 잘못되었습니다."
                return render(req, "login.html", err)

            return HttpResponse(f"<h1>{member.password}</h1>")

        return render(req, 'myproject.html')

def login2(req):
    if req.method == 'GET':
        return render(req, 'myproject.html')
    elif req.method == 'POST':
        useremail = req.POST.get('useremail', None)
        password = req.POST.get('password', None)
        
        err = {}
        if not (useremail and password) :
            err['err'] = '유효성이 잘못되었습니다.'
            return render(req, 'myproject.html', err)
        else:
            member = Members.objects.get(useremail=useremail)
            

            if password == member.password :
                req.session['user'] = member.username
                return redirect('/members')
            else:
                err['err'] = "비밀번호가 잘못되었습니다."
                return render(req, "myproject.html", err)

            return HttpResponse(f"<h1>{member.password}</h1>")

        return render(req, 'myproject.html')



def index(req):
    if req.method == 'GET':
        return render(req, 'myproject.html')
    elif req.method == 'POST':
        
        return redirect('/')

    return render(req, 'myproject.html')

def signup(req):
    if req.method == 'POST' :
        username = req.POST['username']
        useremail = req.POST['useremail']
        password = req.POST['password']

        member = Members(
            username = username,
            useremail = useremail,
            password = password
        )

        member.save()

        res_data = {}
        res_data['res'] ='등록성공'

        return render(req, 'login.html', res_data)
    return render(req, 'signup1.html')
