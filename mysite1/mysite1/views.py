from django.http import HttpResponse, HttpResponseRedirect


def page_2003_view(request):
    html ="<h1> This is the first page </h1>"
    return HttpResponse(html)


def index_view(request):
    html ="<h1> Home Page <h1>"
    return HttpResponse(html)


def page1_view(request):
    html ="<h1> This is page one <h1>"
    return HttpResponse(html)


def page2_view(request):
    html ="<h1> This is page two <h1>"
    return HttpResponse(html)


def pagen_view(request, pg):
    html =f"<h1> This is page {pg}"
    return HttpResponse(html)

def cal_view(request, num1, num2, op):
    res = 0
    if op not in ['sub', 'add', 'mul']:
        return HttpResponse('Wrong URL paramters')
    if op == 'add':
        res = f'{num1} + {num2} = {num1+num2}'
    elif op == 'sub':
        res = f'{num1} - {num2} = {num1-num2}'
    elif op == 'mul':
        res = f'{num1} * {num2} = {num1*num2}'
    return HttpResponse(res)

def cal2_view(request, x, y, op):
    res = 0
    if op not in ['sub', 'add', 'mul']:
        return HttpResponse('Wrong URL paramters')
    if op == 'add':
        res = f'{x} + {y} = {int(x)+int(y)}'
    elif op == 'sub':
        res = f'{x} - {y} = {int(x)-int(y)}'
    elif op == 'mul':
        res = f'{x} * {y} = {int(x)*int(y)}'
    return HttpResponse(f'{res} two digits')


def birthday_view(request, y, m, d):
    res = f'{y}/{m}/{d}'
    return HttpResponse(res)


def test_request(request):
    print('path info: ', request.path_info)
    print('method: ', request.method)
    print('querystring: ', request.GET)
    # return HttpResponse('test request ok', status='200')
    return HttpResponseRedirect('/page/1')