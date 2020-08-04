from django.shortcuts import render
from django.http import HttpResponse
from django.http import StreamingHttpResponse
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
import subprocess
import os
from subprocess import Popen,PIPE,STDOUT


import json



class storeapi(APIView):
    
    def get(self,request):

        st = store.objects.all()
        serializer=storeSerializers(st,many=True)
        return Response(serializer.data)
    def post(self):
        pass

class eventapi(APIView):

    def get(self,request):

        ep = eventpool.objects.all()
        serializer=eventpoolSerializers(ep,many=True)
        return Response(serializer.data)
    def post(self):
        pass


    


@csrf_exempt  
def main_page(request):
        if request.method=='POST':
                received_json_data = json.loads(request.body.decode("utf-8"))
                u = bb(**received_json_data)
                u.save()
                
                framecount=received_json_data['framecount']
                startx=received_json_data['startx']
                starty=received_json_data['starty']
                endx=received_json_data['endx']
                endy=received_json_data['endy']
                in_time=received_json_data['in_time']
                #process = subprocess.Popen(['python','abbcount.py','framecount','startx','starty','endx','endy','in_time'], stdout=PIPE, stderr=STDOUT)
                
                #output = process.stdout.read()
                #exitstatus = process.poll()
                
                #received_json_data=json.loads(request.body)
                return StreamingHttpResponse('it was post request: '+str(received_json_data))
        return StreamingHttpResponse('it was GET request')
            
    
    
    
