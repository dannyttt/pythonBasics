"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # http://127.0.0.1:8000/page/2003/
    path("page/2003/", views.page_2003_view),
    # http://127.0.0.1:8000/
    path("", views.index_view),
    # http://127.0.0.1:8000/page/1
    path("page/1/", views.page1_view),
    # http://127.0.0.1:8000/page/2
    path("page/2/", views.page2_view),
    path("page/<int:pg>", views.pagen_view),
    # re.path regular expression path
    re_path(r"^(?P<x>\d{1,2})/(?P<op>\w+)/(?P<y>\d{1,2})$", views.cal2_view),
    path("<int:num1>/<str:op>/<int:num2>", views.cal_view),
    re_path(
        r"^birthday/(?P<y>\d{4})/(?P<m>\d{1,2})/(?P<d>\d{1,2})$", views.birthday_view
    ),
    path("test_request", views.test_request),
    path("test_get_post", views.test_get_post),
    path("test_html", views.test_html),
    path("test_html_param", views.test_thml_param),
    path("test_if_for", views.test_if_for),
    path("cal_html", views.cal_html),
]
