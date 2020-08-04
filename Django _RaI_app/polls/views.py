from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.utils.timezone import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import StreamingHttpResponse


import json
import plotly.graph_objects as go

from .models import Question,PeopleCount

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def home(request):
    return render(request,'polls/home.html' )



def daily(request):
    fin_list=[]
    curr_year = datetime.utcnow().strftime("%Y")
    curr_mon = datetime.utcnow().strftime("%m")
    curr_date1 = datetime.utcnow().strftime("%d")
    curr_date = datetime.utcnow().strftime("%Y%m%d")
    curr_day=datetime.utcnow()
    curr_day2=datetime.utcnow().strftime("%A")
    print(curr_date,curr_year,curr_mon,curr_date1,curr_day,curr_day2)

    for t in range(10, 22):
        queryset=PeopleCount.objects.filter(in_time__year=curr_year).filter(in_time__month=curr_mon).filter(in_time__day=curr_date1).filter(in_time__hour=t)
        in_count_hourly_list=[q.in_count for q in queryset]      
        in_count_summed=sum(in_count_hourly_list)
        fin_list.append(in_count_summed)

    x = ['10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00','22:00']
    y = fin_list
    my_context={
        "label":x,
        "dataval":y
    }
    return render(request,'polls/chart.html',my_context)

def weekly(request):
    fin_list=[]
    curr_year = datetime.utcnow().strftime("%Y")
    curr_mon = datetime.utcnow().strftime("%m")
    curr_day=datetime.utcnow().strftime("%A")
    curr_date1 = datetime.utcnow().strftime("%d")

    for t in range (int(curr_date1)-7,int(curr_date1)):
        queryset=PeopleCount.objects.filter(in_time__year=curr_year).filter(in_time__month=curr_mon).filter(in_time__day=t)
        in_day_count_list=[q.in_count for q in queryset]
        in_day_count_summed=sum(in_day_count_list)
        fin_list.append(in_day_count_summed)
        print(fin_list)

    x= ['Sun', 'Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat']
    y= fin_list
    my_context={
        "label":x,
        "dataval":y
    }
    return render(request,'polls/weekly.html',my_context)

def monthly(request):
    fin_list=[]
    curr_year = datetime.utcnow().strftime("%Y")
    
    for t in range(1, 13):
        queryset=PeopleCount.objects.filter(in_time__year=curr_year).filter(in_time__month=t)
        in_count_monthly_list=[q.in_count for q in queryset]      
        in_count_summed=sum(in_count_monthly_list)
        fin_list.append(in_count_summed)
    
    x = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    y = fin_list
    my_context={
        "label":x,
        "dataval":y
    }
    
    return render(request,'polls/monthly.html',my_context)

def chart(request):
    fin_list=[]
    curr_date = datetime.utcnow().strftime("%Y%m%d")
    print(curr_date)

    for t in range(10, 22):
        queryset=PeopleCount.objects.filter(in_time__year=2019).filter(in_time__month='09').filter(in_time__day='07').filter(in_time__hour=t)
        in_count_hourly_list=[q.in_count for q in queryset]      
        in_count_summed=sum(in_count_hourly_list)
        fin_list.append(in_count_summed)

    x = ['10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00','22:00']
    y = fin_list
    my_context={
        "label":x,
        "dataval":y
    }
    
    return render(request,'polls/chart.html',my_context)

@csrf_exempt  
def main_page1(request):
        if request.method=='POST':
                received_json_data = json.loads(request.body.decode("utf-8"))
                u = PeopleCount(**received_json_data)
                u.save()
                #received_json_data=json.loads(request.body)
                return StreamingHttpResponse('it was post request: '+str(received_json_data))
        return StreamingHttpResponse('it was GET request')

