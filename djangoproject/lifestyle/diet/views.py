""" in this project we have 9 html pages. 8 out of 9 page are continues multiple html and own_admin_page
is a admin page that provide searching through users.
"""

from django.shortcuts import render
from .models import User
from .bmicalculation import BmiCalculation
from django.db.models import F


def home(request):
    return render(request, 'diet/homepage.html')


def login(request):
    return render(request, 'diet/login.html')


def bmi(request):
    # it checks validation of user from previous page and has two results.
    login_username, login_password = request.POST.get("user"), request.POST.get("pass")
    user_data_check = User.objects.filter(username=login_username).count()
    # if checks the user is new or logged before.
    if user_data_check >= 1:
        #  user logged before hence shows his/her previous inputted data
        user_data_from_DB = (list(User.objects.filter(username=login_username).values()))[0]
        return render(request, 'diet/repetitive_user.html', {'user_data_from_DB': user_data_from_DB})
    else:
        # user is new ,and it gets rest of his/her data(here calculate the BMI). Multiple html pages start here.
        request.session['user'], request.session['pass'] = login_username, login_password
        return render(request, 'diet/bmi.html')


def result(request):
    if request.method == "POST":
        # here calculate the bmi of users.
        height, weight = request.POST.get('height'), request.POST.get('weight')
        bmi_object = BmiCalculation(height, weight)
        result_dict = {'bmi_number': bmi_object.bmi_calculation(), 'bmi_massage': bmi_object.bmi_massage()}
        # bmi validation decide who to entrance.
        if bmi_object.entrance_validation() == 1:
            #  not allowed user to entrance.
            return render(request, 'diet/badresult.html', {'result_dict': result_dict})
        else:
            # allowed user to entrance.
            return render(request, 'diet/result.html', {'result_dict': result_dict})
    else:
        return render(request, "diet/badresult.html")


def info(request):
    return render(request, 'diet/info.html')


def contact(request):
    name, fname = request.POST.get('name'), request.POST.get('fname')
    request.session['name'], request.session['fname'] = name, fname
    return render(request, 'diet/contact.html')


def lifestyle(request):
    email, phone = request.POST.get('email'), request.POST.get('phone')
    request.session['email'], request.session['phone'] = email, phone
    return render(request, 'diet/lifestyle.html')


def suggestion(request):
    # in suggestion, we will see food offer and brief inputted result
    # it suggests the food
    life = request.POST.get("lifestylediet")
    request.session['lifestyles'] = life
    if life == "veg":
        food = "Vegetable Soup"
    else:
        food = "Butter Chicken"
    #     it saves user history data.
    final_result_from_DB = {'food': food,
                            'name': request.session['name'],
                            'fname': request.session['fname'],
                            'email': request.session['email'],
                            'phone': request.session['phone']
                            }
    # save user data in DB
    DB_object = User(username=request.session['user'], password=request.session['pass'], bmi=request.session['bmi'],
                     name=request.session['name'], fname=request.session['fname'], email=request.session['email'],
                     contact=request.session['phone'], veg_type=request.session['lifestyles'])
    DB_object.save()
    return render(request, 'diet/suggestion.html', {'final_result_from_DB': final_result_from_DB})


def logout(request):
    return render(request, 'diet/logout.html')


def own_admin_page(request):
    # this is a adminpage
    if request.method == "POST":
        # here we searching for users
        if request.POST.get('search_word') != "":
            search_word = request.POST.get('search_word')
            result = list(User.objects.filter(username__contains=search_word))
            return render(request, 'diet/own_adminpage.html', {'result': result})
        else:
            # here we see all user
            result = list(User.objects.all())
            return render(request, 'diet/own_adminpage.html', {'result': result})
    else:
        order_by = request.GET.get('order_by')
        direction = request.GET.get('direction')
        print(order_by, direction)
        if order_by and direction:
            if direction == 'desc':
                order_by = '-{}'.format(order_by)
            result=list(User.objects.all().order_by(order_by))
            return render(request, 'diet/own_adminpage.html', {'result': result})
        else:
            result = list(User.objects.all())
            print(result)
            return render(request, 'diet/own_adminpage.html', {'result': result})

