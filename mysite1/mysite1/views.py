from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

POST_FORM = """
    <form method='post' action='/test_get_post'>
        username: <input type='text' name='uname'>
        <input type='submit' value='submit'>
    </form>

"""


def page_2003_view(request):
    html = "<h1> This is the first page </h1>"
    return HttpResponse(html)


def index_view(request):
    html = "<h1> Home Page <h1>"
    return HttpResponse(html)


def page1_view(request):
    html = "<h1> This is page one <h1>"
    return HttpResponse(html)


def page2_view(request):
    html = "<h1> This is page two <h1>"
    return HttpResponse(html)


def pagen_view(request, pg):
    html = f"<h1> This is page {pg}"
    return HttpResponse(html)


def cal_view(request, num1, num2, op):
    res = 0
    if op not in ["sub", "add", "mul"]:
        return HttpResponse("Wrong URL paramters")
    if op == "add":
        res = f"{num1} + {num2} = {num1+num2}"
    elif op == "sub":
        res = f"{num1} - {num2} = {num1-num2}"
    elif op == "mul":
        res = f"{num1} * {num2} = {num1*num2}"
    return HttpResponse(res)


def cal2_view(request, x, y, op):
    res = 0
    if op not in ["sub", "add", "mul"]:
        return HttpResponse("Wrong URL paramters")
    if op == "add":
        res = f"{x} + {y} = {int(x)+int(y)}"
    elif op == "sub":
        res = f"{x} - {y} = {int(x)-int(y)}"
    elif op == "mul":
        res = f"{x} * {y} = {int(x)*int(y)}"
    return HttpResponse(f"{res} two digits")


def birthday_view(request, y, m, d):
    res = f"{y}/{m}/{d}"
    return HttpResponse(res)


def test_request(request):
    print("path info: ", request.path_info)
    print("method: ", request.method)
    print("querystring: ", request.GET)
    # return HttpResponse('test request ok', status='200')
    return HttpResponseRedirect("/page/1")


# ==================================================================
# Day 2, GET POST method
def test_get_post(request):
    if request.method == "GET":
        # print(request.GET["username"])
        print(request.GET)
        print(request.GET.getlist("a"))
        print(request.GET.get("password", "no password"))
        # .getlist
        return HttpResponse(POST_FORM)
    elif request.method == "POST":
        print(f'username: {request.POST["uname"]}')
        return HttpResponse("200 ok")
    else:
        pass
    return HttpResponse("test get post is ok 200")


# render page method 1
# def test_html(request):
#     from django.template import loader

#     t = loader.get_template("test_html.html")
#     html = t.render()
#     return HttpResponse(html)


# render page method 2


def test_html(request):

    dic = {"username": "meiumi", "age": 18}
    return render(request, "test_html.html", dic)


def test_thml_param(request):

    dic = {}
    dic["int"] = 88
    dic["str"] = "meiumi"
    dic["list"] = ["Tom", "Jack", "Lily"]
    dic["dict"] = {"a": 9, "b": 8}
    dic["func"] = say_hi
    dic["class_obj"] = Dog()

    return render(request, "test_html_param.html", dic)


def test_if_for(request):

    dic = {}
    dic["x"] = 10
    return render(request, "test_if_for.html", dic)


def cal_html(request):
    if request.method == "GET":
        return render(request, "cal_html.html")
    elif request.method == "POST":
        # dic = {}
        x = int(request.POST["x"])
        y = int(request.POST["y"])
        res = 0
        opsign = request.POST["opsign"]
        if opsign == "add":
            res = x + y
        elif opsign == "sub":
            res = x - y
        elif opsign == "mul":
            res = x * y
        elif opsign == "div":
            res = x / y
        # dic["res"] = res
        # dic["x"] = x
        # dic["y"] = y
        return render(request, "cal_html.html", locals())


def say_hi():
    return "hello"


class Dog:
    def say(self):
        return "wurf wurf"
