import plotly.graph_objects as go
from polls.models import PeopleCount

# from .models import Question,PeopleCount

fin_list=[]
for t in range(10, 22):

        queryset=PeopleCount.objects.filter(in_time__year=2019).filter(in_time__month='09').filter(in_time__day='05').filter(in_time__hour=t)
        in_count_hourly_list=[q.in_count for q in queryset]      
        in_count_summed=sum(in_count_hourly_list)
        fin_list.append(in_count_summed)
        print(fin_list)
        
        json_hr_count = json.dumps(fin_list)
        print(json_hr_count)

x = ['Sunday','Monday','Tuesday' ,'Wednesday','Thursday','Friday','Saturday']
y = [20, 14, 23]

x = ['10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00','22:00']
y = fin_list

# Use textposition='auto' for direct text
fig = go.Figure(data=[go.Bar(
            x=x, y=y,
            text=y,
            textposition='auto',
        )])

fig.show()




