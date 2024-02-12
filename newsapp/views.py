from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages,auth
from django.contrib.auth import authenticate
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request, 'index.html')

def staffregister(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        mob = request.POST['phone']
        password = request.POST['password']
        address = request.POST['address']
        img = request.FILES['img']
        age=request.POST['age']
        qualification=request.POST['qualification']
        if Staff_reg.objects.filter(email=email).exists():
            messages.info(request, "email already exists")
        else:
            staff = Login.objects.create_user(
                username=email, password=password, usertype='staff', ViewPassword=password, is_active=1)
            staff.save()
            register = Staff_reg.objects.create(
                name=name, email=email, img=img, phone=mob, age=age, staff=staff, address=address, qualification=qualification)
            register.save()
            messages.info(request, "registration successfull")
            return redirect("/adminviewstaff")

    return render(request, 'admin/addstaff.html')


def officerregister(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        mob = request.POST['phone']
        password = request.POST['password']
        address = request.POST['address']
        img = request.FILES['img']
        age=request.POST['age']
        qualification=request.POST['qualification']
        if Officer_reg.objects.filter(email=email).exists():
            messages.info(request, "email already exists")
        else:
            officer = Login.objects.create_user(
                username=email, password=password, usertype='officer', ViewPassword=password, is_active=1)
            officer.save()
            register = Officer_reg.objects.create(
                name=name, email=email, img=img, phone=mob, age=age, officer=officer, address=address, qualification=qualification)
            register.save()
            messages.info(request, "registration successfull")
            return redirect("/login")

    return render(request, 'admin/addofficer.html')

def userregister(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        mob = request.POST['phone']
        password = request.POST['password']
        address = request.POST['address']
        img = request.FILES['img']
        age=request.POST['age']
        gender=request.POST['gender']
        qualification=request.POST['qualification']
        if User_reg.objects.filter(email=email).exists():
            messages.info(request, "email already exists")
        else:
            user = Login.objects.create_user(
                username=email, password=password, usertype='user', ViewPassword=password, is_active=1)
            user.save()
            register = User_reg.objects.create(
                name=name, email=email, img=img, phone=mob, age=age, user=user, address=address, qualification=qualification,gender=gender)
            register.save()
            messages.info(request, "registration successfull")
            return redirect("/login")

    return render(request, 'user/registration.html')


def login(request):
    if request.POST:

        email = request.POST["email"]
        password = request.POST["password"]
        # print(email, password,"test")
        user = authenticate(username=email, password=password)
        # print("trxdetxtrx",user)
        if user is not None:
            if user.usertype == "admin":
                messages.info(request, "welocme to  page admin")
                return redirect('/admin1')

            elif user.usertype == "user":
                print(user.usertype)
                request.session['uid'] = user.id
                messages.info(request, "welcome to user page")
                return redirect('/userhome')
            elif user.usertype == "officer":
                print(user.usertype)
                request.session['uid'] = user.id
                messages.info(request, "welcome to officer page")
                return redirect('/officerhome')
            elif user.usertype == "staff":
                request.session['uid'] = user.id
                messages.info(request, "welcome to staff page")
                print(user.usertype)
                return redirect('/staffhome')
            else:
                messages.info(request, "invalid login")
        else:
            # messages.info(request, "User Not Approved")
            print("Type Not Get")
    return render(request,'login.html')


def admin1(request):
    return render(request,'admin/adminhome.html')

def staffhome(request):
    return render(request,'staff/home.html')
def officerhome(request):
    news=UserActions.objects.filter(status="unread").count()
    return render(request,'officer/home.html',{'news':news})

def userhome(request):
    news = Add_news.objects.order_by('-date', '-time')[:5] 
    flash=Add_news.objects.filter(status="flash")
    return render(request,'user/userhome.html',{'news':news,'flash':flash})

def addnews(request):
    sid=request.session['uid']
    Sid=Staff_reg.objects.get(staff=sid)
    if request.POST:
        name=request.POST['name']
        category=request.POST['category']
        description=request.POST['description']
        img=request.FILES['img']
        date=request.POST['date']
        time=request.POST['time']
        district=request.POST['district']
        
        news=Add_news.objects.create(name=name,category=category,description=description,date=date,time=time,district=district,img=img,sid=Sid)
        news.save()
        return redirect('/staffhome')
    return render(request,'staff/addnews.html')
        
        

def delete(request):
    a=Login.objects.filter(usertype="staff")
    a.delete()
   
   
def staffaddnews(request):
    sid=request.session['uid']
    Sid=Staff_reg.objects.get(staff=sid)
    print(Sid,'aaaaaaaaa')
    if request.POST:
        name=request.POST['name']
        category=request.POST['category']
        description=request.POST['discription']
        img=request.FILES['img']
        date=request.POST['date']
        time=request.POST['time']
        district=request.POST['district']
        
        news=Add_news.objects.create(name=name, category=category, description=description, img=img, date=date, time=time, district=district,sid=Sid)
        news.save()
        
    return render(request,'staff/addnews.html')

def adminviewstaff(request):
    staff=Staff_reg.objects.all()
    return render(request, 'admin/viewstaff.html',{'staff':staff})


def admindeletestaff(request):
    sid=request.GET.get('sid')
    staff=Staff_reg.objects.filter(id=sid)
    staff.delete()
    staff1=Login.objects.filter(id=sid)
    staff1.delete()
    return redirect('/adminviewstaff')

def officerviewnews(request):
    news=Add_news.objects.all()
    return render(request,'officer/viewnews.html',{'news':news})

def logout(request):
    auth.logout(request)
    return redirect('/')



def adminviewofficer(request):
    officer=Officer_reg.objects.all()
    return render(request,'admin/viewofficer.html',{'officer':officer})


def viewnewsaction(request):
    status=request.GET['status']
    id=request.GET['id']
    news=Add_news.objects.get(id=id)
    news.status=status
    news.save()
    if status == "accepted":
        messages.info(request,"accepted successfully")
    elif status == "flash":
        messages.info(request,"news accepted as flash news")
    
    else:
        messages.info(request,"news rejected")
    return redirect('/officerviewnews')


def officerdeletenews(request):
    id=request.GET.get('id')
    news=Add_news.objects.filter(id=id).delete()
    messages.info(request,"news deleted successfully")
    return redirect('/officerviewnews')

def officerviewcategory(request):
    return render(request,'officer/viewcategory.html')


def userviewcategory(request):
    return render(request,'user/viewcategory.html')

# def userviewpoliticalnews(request):
#     news = Add_news.objects.filter(Q(status="accepted") & Q(category="politics") & Q(status="flash"))
#     return render(request,'user/viewpoliticalnews.html',{'news':news})
# def userviewcorporatenews(request):
#     news = Add_news.objects.filter(Q(status="accepted") & Q(category="corporate") & Q(status="flash"))
#     return render(request,'user/viewpoliticalnews.html',{'news':news})
# def userviewhealthnews(request):
#     news=Add_news.objects.filter(Q(status="accepted") & Q(category="entertainment") & Q(status="flash"))
#     return render(request,'user/viewpoliticalnews.html',{'news':news})
# def uservieweducationnews(request):
#     news = Add_news.objects.filter(Q(status="accepted") & Q(category="education") & Q(status="flash"))
#     return render(request,'user/viewpoliticalnews.html',{'news':news})
# def userviewentertainmentnews(request):
#     news = Add_news.objects.filter(Q(status="accepted") & Q(category="entertainment") & Q(status="flash"))
#     return render(request,'user/viewpoliticalnews.html',{'news':news})
# def userviewbusinessnews(request):
#     news = Add_news.objects.filter(Q(status="accepted") & Q(category="business") & Q(status="flash"))
#     return render(request,'user/viewpoliticalnews.html',{'news':news})
# def userviewsciencenews(request):
#     news = Add_news.objects.filter(Q(status="accepted") & Q(category="science") & Q(status="flash"))
#     return render(request,'user/viewpoliticalnews.html',{'news':news})
# def userviewfoodnews(request):
#     news = Add_news.objects.filter(Q(status="accepted") & Q(category="food") & Q(status="flash"))
#     return render(request,'user/viewpoliticalnews.html',{'news':news})
# def userviewtravelnews(request):
#     news = Add_news.objects.filter(Q(status="accepted") & Q(category="travel") & Q(status="flash"))
#     return render(request,'user/viewpoliticalnews.html',{'news':news})


def userviewnewsdetails(request):
    uid=request.session['uid']
    id=request.GET.get('id')
    print(uid,id)
    Uid=User_reg.objects.filter(user__id=uid)
    print(Uid[0].id,"aaaaaaaaaaaaaaaaaaaaa")
    news=Add_news.objects.filter(id=id)
    comment=Usercomment.objects.filter(id=id)
    if request.POST:
        action=request.POST['comment']
        comment=request.POST['comment']
        Uid=User_reg.objects.get(id=Uid[0].id)
        nid=Add_news.objects.get(id=id)
        user=Usercomment.objects.create(uid=Uid,comment=comment)
        user.save()
        user1=UserActions.objects.create(uid=Uid,comment=action)
        user1.save()
        like=Likenews.objects.create(uid=Uid,nid=nid)    
        like.save()
        dislike=Dislikenews.objects.create(uid=Uid,nid=nid)    
        dislike.save()
        
        messages.info(request,"successfully comented")
    return render(request,'user/viewnewsdetails.html',{'news':news,'comment':comment})

def staffviewcategory(request):
    return render(request,'staff/viewcategory.html')

def staffviewnews(request):
    return render(request,'staff/viewnews.html')

def staffviewpoliticalnews(request):
    id=request.session['uid']
    print(id,"aannnnnnnnn")
    sid=Staff_reg.objects.get(staff=id)
    print(sid.id,"qqqqqqqqqqq")
    
    news=Add_news.objects.filter(sid=sid.id,category="politics")
    return render(request,'staff/viewpoliticalnews.html',{'news':news})
def staffupdatenews(request):
    sid=request.session['uid']
    nid=request.GET.get('nid')
    Sid=Staff_reg.objects.get(staff=sid)
    News=Add_news.objects.filter(id=nid)
    
    update = Add_news.objects.filter(id=nid)
    if request.POST:
        if 'img' in request.FILES:
            img=request.FILES['img']
        else:
            img=update[0].img
        name = request.POST.get("name")
        # img = request.FILES["img"]
        description=request.POST.get("description")
        category=request.POST.get("category")
        date=request.POST.get("date")
        time=request.POST.get("time")
        district=request.POST.get("district")

        updatedata = Add_news.objects.get(id=nid)
        updatedata.img = img
      
        updatedata.description=description
        updatedata.name=name
        updatedata.category=category
        updatedata.date=date
        updatedata.time=time
        updatedata.district=district
        updatedata.save()
        messages.info(request," update news successfuly")
        return redirect('/staffviewnews')
    return render(request,'staff/updatenews.html',{'update':update})

def staffdeletenews(request):
    id=request.session['uid']
    nid=request.GET.get('nid')
    sid=Staff_reg.objects.get(staff=id)
    news=Add_news.objects.filter(id=nid)
    news.delete()
    messages.info(request,"news deleted successfully")
    return redirect('/staffviewnews')   
def staffviewbusinessnews(request):
    id=request.session['uid']
    print(id,"aannnnnnnnn")
    sid=Staff_reg.objects.get(staff=id)
    news2=Add_news.objects.filter(sid=sid.id,category="business")
    return render(request,'staff/businessnews.html',{'news2':news2})

def staffviewcorporatenews(request):
    id=request.session['uid']
    print(id,"aannnnnnnnn")
    sid=Staff_reg.objects.get(staff=id)
    news3=Add_news.objects.filter(sid=sid.id,category="corporate")
    return render(request,'staff/corporatenews.html',{'news3':news3})
def staffviewhealthnews(request):
    id=request.session['uid']
    print(id,"aannnnnnnnn")
    sid=Staff_reg.objects.get(staff=id)
    news6=Add_news.objects.filter(sid=sid.id,category="health")
    return render(request,'staff/healthnews.html',{'news6':news6})

def staffviewtravelnews(request):
    id=request.session['uid']
    print(id,"aannnnnnnnn")
    sid=Staff_reg.objects.get(staff=id)
    news9=Add_news.objects.filter(sid=sid.id,category="travel")
    return render(request,'staff/travelnews.html',{'news9':news9})

def staffviewfoodnews(request):
    id=request.session['uid']
    print(id,"aannnnnnnnn")
    sid=Staff_reg.objects.get(staff=id)
    news4=Add_news.objects.filter(sid=sid.id,category="food")
    return render(request,'staff/foodnews.html',{'news4':news4})

def staffvieweducationnews(request):
    id=request.session['uid']
    print(id,"aannnnnnnnn")
    sid=Staff_reg.objects.get(staff=id)
    news8=Add_news.objects.filter(sid=sid.id,category="education")
    return render(request,'staff/educationnews.html',{'news8':news8})

def staffviewsciencenews(request):
    id=request.session['uid']
    print(id,"aannnnnnnnn")
    sid=Staff_reg.objects.get(staff=id)
    news7=Add_news.objects.filter(sid=sid.id,category="science")
    return render(request,'staff/sciencenews.html',{'news7':news7})

def staffviewentertainmentnews(request):
    id=request.session['uid']
    print(id,"aannnnnnnnn")
    sid=Staff_reg.objects.get(staff=id)
    news5=Add_news.objects.filter(sid=sid.id,category="entertaiment")
    return render(request,'staff/entertainmentnews.html',{'news5':news5})

def viewnotification(request):
    notification=UserActions.objects.all()
    return render(request,'officer/viewnotification.html',{'notification':notification})

def adminviewnews(request):
    politics=Add_news.objects.filter(category="politics")
    corporate=Add_news.objects.filter(category="corporate")
    business=Add_news.objects.filter(category="business")
    food=Add_news.objects.filter(category="food")
    entertainment=Add_news.objects.filter(category="entertainment")
    health=Add_news.objects.filter(category="health")
    science=Add_news.objects.filter(category="science")
    travel=Add_news.objects.filter(category="travel")
    education=Add_news.objects.filter(category="education")
    
    
    return render(request,'admin/viewnews.html',{'politics':politics, 'science':science, 'travel':travel,'corporate':corporate, 'education':education,'business':business,'food':food,'health':health, 'entertainment':entertainment})

    
    
    
def adminviewcategory(request):
    return render(request,'admin/viewcategory.html') 


def officerviewnotification(request):
    view=UserActions.objects.all()
    print(view)
    return render(request,'officer/viewnotification.html',{'view':view})

def userviewdistrictnews(request):
    name=request.GET.get('name')
    print(name)
    news=Add_news.objects.filter((Q(status="accepted") | Q(status="flash")) & Q(district__iexact=name))
    return render(request,'user/viewdistrictnews.html',{'news':news})
    
def notificationaction(request):
    status=request.GET['status']
    id=request.GET['id']
    news=UserActions.objects.get(id=id)
    news.status=status
    news.save()
    if status == "read":
        messages.info(request,"Read successfully")
    
    else:
        messages.info(request,"rejected")
    return redirect('/officerviewnotification')

def deletenotification(request):
    nid=request.GET.get('nid')
    notification=UserActions.objects.filter(id=nid)
    notification.delete()
    return redirect('/officerviewnotification')
    
def userviewcategorynews(request):
    name=request.GET.get('name')
    news=Add_news.objects.filter((Q(status="accepted") | Q(status="flash")) & Q(category__iexact=name))
    return render(request,'user/viewcategorynews.html',{'news':news})
    
def userviewprofile(request):
    uid=request.session['uid']
    print(uid,"aaaaaaaaaa")
    user=User_reg.objects.filter(user=uid)
    return render(request,'user/viewprofile.html',{'user':user})

# def userlike(request):
#     uid=request.session['uid']
#     Uid=User_reg.objects.filter(user=uid)
#     nid=request.GET.get('nid')
#     if request.POST:
#         like=Likenews.objects.create(uid=Uid,nid=nid)    
#         like.save()
#         return redirect('/userviewnewsdetail')

# def userdislike(request):
#     uid=request.session['uid']
#     Uid=User_reg.objects.filter(user=uid)
#     nid=request.GET.get('nid')
#     if request.POST:
        
#         dislike=Dislikenews.objects.create(uid=Uid,nid=nid)    
#         dislike.save()
#         return redirect('/userviewnewsdetail')

    
