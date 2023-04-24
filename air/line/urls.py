from django.contrib import admin
from django.urls import path
from line import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about", views.about, name="about"),
    path("checkflight", views.checkflight, name="checkflight"),
    path("contact_", views.contact_, name="contact_"),
    path("bookflight", views.bookflight, name="bookflight"),
    path("flightschedule", views.flightschedule, name="flightschedule"),
    path("adminuse", views.adminuse, name="adminuse"),
    path("login",views.handlelogin,name="handlelogin"),
    path("logout",views.handlelogout,name="handlelogout"),
    path("adminpanel",views.adminpanel,name="adminpanel"),
    path("addflights",views.addflights,name="addflights"),
    path("delflight",views.delflight,name="delflight"),
    path("delete/<int:id>",views.delete,name="delete"),
    path("cancelflight/<int:id>",views.cancelflight,name="cancelflight"),
]
