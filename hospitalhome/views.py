from django.shortcuts import render
import mysql.connector
from django.core.files.storage import FileSystemStorage
from datetime import date



# Create your views here.

def home(request):
    return render(request, 'home.html')

def adminlogin(request):
    return render(request, 'adminlogin.html')

def adminloginvalidater(request):
    a=request.GET.get('usern')
    b=request.GET.get('pass')
    if a=='admin' and b=='admin':
        return render(request, 'adminhome.html')
    else:
        error='check username and password'
        return render(request, 'adminlogin.html',{'err':error})
    return render(request, 'adminlogin.html',{'err':error})
def adminhome(request):
    return render(request, 'adminhome.html')

def admindoctorrequest(request):
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='vitalhospitaldb')
    mycursor=mydb.cursor()
    q='select*from doctor where status="create"'
    mycursor.execute(q)
    row=mycursor.fetchall()
    mydb.close()

    return render(request,'admindoctorrequest.html',{'request':row})
def adminapprovedoctor(request):
    a=request.GET.get('reqid')
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='vitalhospitaldb')
    mycursor=mydb.cursor()
    q='update doctor set status="approved" where doctorid="'+a+'"'
    mycursor.execute(q)
    mydb.commit()
    mydb.close()
    return admindoctorrequest(request)
def adminselecteddoctorview(request):
     mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='vitalhospitaldb')
     mycursor=mydb.cursor()
     q='select*from doctor where status="approved"'
     mycursor.execute(q)
     row=mycursor.fetchall()
     mydb.close()

     return render(request,'adminselectdoctor.html',{'request':row})

def admindeletedoctor(request):
    a=request.GET.get('reqid')
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='vitalhospitaldb')
    mycursor=mydb.cursor()
    q='delete from doctor where doctorid="'+a+'"'
    mycursor.execute(q)
    mydb.commit()
    mydb.close()
    return adminselecteddoctorview(request)







#patient
def patientlogin (request):
    return render(request,'patientlogin.html')

def patientregister(request):
    return render(request,'patientregister.html')

def patientregistervalidater(request):
    drname=request.GET.get('dname')
    drgender=request.GET.get('dgender')
    drspecialization=request.GET.get('dob')
    dreducation=request.GET.get('phone')
    dreperence=request.GET.get('mail')
    draddress=request.GET.get('daddress')
    drusername=request.GET.get('dusername') 
    dpassword=request.GET.get('dpassword')  
    day=date.today()
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='vitalhospitaldb') 
    mycursor=mydb.cursor()
    check='select*from patient where email="'+dreperence+'" '
    mycursor.execute(check)
    checkvalue=mycursor.fetchone()
    if checkvalue is None:
        q='insert into patient (name,gender,date_of_birth,phone,email,address,date,username,password)values("'+str(drname)+'","'+str(drgender)+'","'+str(drspecialization)+'","'+str(dreducation)+'","'+str(dreperence)+'","'+str(draddress)+'","'+str(day)+'","'+str(drusername)+'","'+str(dpassword)+'")'
        mycursor.execute(q)
        print(q)
        mydb.commit()
        mydb.close()
        return render(request,'patientlogin.html')
    else:
        return render(request,'patientregister.html',{'regerror':'alredy register '})

        
    


def patientloginvalidater(request):
    pname=request.GET.get('usern')
    ppass=request.GET.get('pass')
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='vitalhospitaldb') 
    mycursor=mydb.cursor()
    q='select*from patient where username="'+pname+'" and password="'+ppass+'"'
    mycursor.execute(q)
    print(q)
    row=mycursor.fetchone()
    mydb.close()
    if row is  None: 
         return render(request,'patientlogin.html',{'err':'login not match'} )
         
    else:

        request.session['patientid']=row[0]
        request.session['patientname']=row[1]
        return render(request,'patienthome.html',{'patientname': request.session['patientname']})
         




    

   


#doctor

def doctorlogin(request):
    return render(request,'doctorlogin.html')

def doctorregister(request):
    return render(request,'doctorregister.html')

    
def doctorregesterform(request):
    drname=request.GET.get('dname')
    drgender=request.GET.get('dgender')
    drspecialization=request.GET.get('dspecialization')
    dreducation=request.GET.get('deducation')
    dreperence=request.GET.get('dexperence')
    draddress=request.GET.get('daddress')
    drusername=request.GET.get('dusername') 
    dpassword=request.GET.get('dpassword')  
    day=date.today()
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='vitalhospitaldb') 
    mycursor=mydb.cursor()
    check='select*from doctor where username="'+drusername+'" and password="'+dpassword+'" '
    mycursor.execute(check)
    checkvalue=mycursor.fetchone()
    if checkvalue is None:
        q='insert into doctor (name,gender,specialization,education,experience,address,date,username,password)values("'+str(drname)+'","'+str(drgender)+'","'+str(drspecialization)+'","'+str(dreducation)+'","'+str(dreperence)+'","'+str(draddress)+'","'+str(day)+'","'+str(drusername)+'","'+str(dpassword)+'")'
        mycursor.execute(q)
        print(q)
        mydb.commit()
        mydb.close()
        return render(request,'doctorlogin.html')
    else:
        return render(request,'doctorregister.html',{'erreg':'alredy exist'})

def doctorloginvalidater(request):
     dname=request.GET.get('usern')
     dpass=request.GET.get('pass')
     mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='vitalhospitaldb') 
     mycursor=mydb.cursor()
     q='select*from doctor where username="'+dname+'" and password="'+dpass+'"'
     mycursor.execute(q)
     print(q)
     row=mycursor.fetchone()
     mydb.close()
     if row is  None: 
          return render(request,'doctorlogin.html',{'err':'login not match'} )
         
     else:

         request.session['doctorid']=row[0]
         request.session['doctorname']=row[1]
         return render(request,'doctorhome.html',{'doctorname': request.session['doctorname']})
     
def doctorhome(request):
    return render(request,'doctorhome.html',{'doctorname':request.session['doctorname']})     

         



    


    


