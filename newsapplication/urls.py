"""
URL configuration for newsapplication project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from newsapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('userregister/',views.userregister),
    path('staffregister/',views.staffregister),
    path('officerregister/',views.officerregister),
    path('login/',views.login),
    path('addnews/',views.addnews),
    path('admin1/',views.admin1),
    path('userhome/',views.userhome),
    path('staffhome/',views.staffhome),
    path('officerhome/',views.officerhome),
    # path('adminaddofficer/',views.adminaddofficer),
    path('staffaddnews/',views.staffaddnews),
    path('adminviewstaff/',views.adminviewstaff),
    path('admindeletestaff/',views.admindeletestaff),
    path('officerviewnews/',views.officerviewnews),
    path('logout/',views.logout),
    path('adminviewofficer/',views.adminviewofficer),
    path('viewnewsaction/',views.viewnewsaction),
    path('officerdeletenews/',views.officerdeletenews),
    path('officerviewcategory/',views.officerviewcategory),
    path('delete/',views.delete),
    path('userviewcategory/',views.userviewcategory),
    # path('userviewpoliticalnews/',views.userviewpoliticalnews),
    path('userviewnewsdetails/',views.userviewnewsdetails),
    path('staffviewcategory/',views.staffviewcategory),
    path('staffviewnews/',views.staffviewnews),
    path('staffviewpoliticalnews/',views.staffviewpoliticalnews),
    path('staffupdatenews/',views.staffupdatenews),
    path('staffdeletenews/',views.staffdeletenews),
    path('staffviewbusinessnews/',views.staffviewbusinessnews),
    path('staffviewcorporatenews/',views.staffviewcorporatenews),
    path('staffviewhealthnews/',views.staffviewhealthnews),
    path('staffvieweducationnews/',views.staffvieweducationnews),
    path('staffviewsciencenews/',views.staffviewsciencenews),
    path('staffviewentertainmentnews/',views.staffviewentertainmentnews),
    path('staffviewfoodnews/',views.staffviewfoodnews),
    path('staffviewtravelnews/',views.staffviewtravelnews),
    path('viewnotification/',views.viewnotification),
    path('adminviewnews/',views.adminviewnews),
    path('adminviewcategory/',views.adminviewcategory),
    path('officerviewnotification/',views.officerviewnotification),
    # path('userviewentertainmentnews/',views.userviewentertainmentnews),
    # path('userviewsciencenews/',views.userviewsciencenews),
    # path('userviewtravelnews/',views.userviewtravelnews),
    # path('uservieweducationnews/',views.uservieweducationnews),
    # path('userviewbusinessnews/',views.userviewbusinessnews),
    # path('userviewcorporationnews/',views.userviewcorporatenews),
    # path('userviewhealthnews/',views.userviewhealthnews),
    # path('userviewfoodnews/',views.userviewfoodnews),
    # # path('latestnews/',views.latestnews),
    path('userviewdistrictnews/',views.userviewdistrictnews),
    path('deletenotification/',views.deletenotification),
    path('notificationaction/',views.notificationaction),
    path('userviewcategorynews/',views.userviewcategorynews),
    path('userviewprofile/',views.userviewprofile),
    
    
    
         
]
