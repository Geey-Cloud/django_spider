from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from login import models
from login.spider_pyecharts import html_pie_sex, html_funnel_level, html_bar_followers, html_pie_vip


def welcome(request):
    """
    欢迎页
    :param request:
    :return:
    """
    return render(request, 'welcome.html')


def login(request):
    """
    登录
    :param request:
    :return:
    """
    name_input = request.POST.get("name")
    password_input = request.POST.get("password")

    if name_input == 'root' and password_input == 'Geey200714':
        users = models.LoginInfo.objects.all()
        return render(request, 'userManagement.html', {'name': name_input, 'users': users})

    user = models.LoginInfo.objects.filter(name=name_input, password=password_input)
    if user.exists():
        # print("登录成功！")
        return render(request, 'spider.html', {'name': name_input})
    else:
        # print("登录失败")
        return render(request, 'login.html')


def register(request):
    """
    注册
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'register.html')

    name = request.POST.get("name")
    password = request.POST.get("password")
    password_check = request.POST.get("password_check")
    name_ = models.LoginInfo.objects.filter(name=name)
    if password == password_check and len(name) != 0 and len(password) != 0 and not name_.exists():
        # 添加到数据库
        models.LoginInfo.objects.create(name=name, password=password)
        # messages.error(request, "登录成功！")
        return redirect('/register')
    else:
        messages.error(request, "用户名或密码错误！")
        return redirect('/register')


def spider(request):
    """
    数据展示
    :param request:
    :return:
    """
    user_number = models.UserInfo.objects.all().count()
    html_pie_sex()
    html_funnel_level()
    html_bar_followers()
    html_pie_vip()
    return render(request, 'spider.html', locals())


def user_management(request):
    """
    用户管理
    :param request:
    :return:
    """
    users = models.LoginInfo.objects.all()

    return render(request, 'userManagement.html', {'users': users})


def addUser(request):
    """
    添加用户
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'addUser.html')
    name = request.POST.get("name")
    password = request.POST.get("password")
    name_ = models.LoginInfo.objects.filter(name=name)
    print(name_, name)
    if name_.exists() or len(name) == 0 or len(password) == 0:
        messages.error(request, "请重新添加。")
        return render(request, 'addUser.html')
    else:
        # 添加到数据库
        models.LoginInfo.objects.create(name=name, password=password)
        messages.error(request, "添加成功！")
        return render(request, 'addUser.html')


def deleteUser(request):
    """
    删除用户
    :param request:
    """
    id = request.GET.get('id')
    models.LoginInfo.objects.filter(id=id).delete()
    return redirect('/userManagement')


def pie_sex(request):
    return render(request, 'pie_sex.html')


def funnel_level(request):
    return render(request, 'funnel_level.html')


def bar_followers(request):
    return render(request, 'bar_followers.html')


def pie_vip(request):
    return render(request, 'pie_vip.html')
