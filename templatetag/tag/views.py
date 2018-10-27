from django.shortcuts import render
import datetime
def wish(request):
    date=datetime.datetime.now()
    msg='hello guest !!! very good'
    h=int(date.strftime('%H'))
    if h<12:
        msg+='morning'
    elif h<16:
        msg+='afternoon'
    elif h<21:
        msg+='eveiving'
    else:
        msg='hello guest !!! very good nit'
    my_dict={'insert_date':date,'insert_msg':msg}
    return render(request,'tag/ww.html',context=my_dict)

# Create your views here.
