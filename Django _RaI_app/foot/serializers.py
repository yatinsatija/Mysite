from rest_framework import serializers
from rest_framework import *
from .models import *

class tenantSerializers(serializers.ModelSerializer):
    class Meta:
        model=tenant
        fields='__all__'

class staffSerializers(serializers.ModelSerializer):
    class Meta:
        model=staff
        fields=['name','contact_number','sex','age','designation']  
class cameraSerializers(serializers.ModelSerializer):
   
    class Meta:
        model=camera
        fields='__all__'

class storeSerializers(serializers.ModelSerializer):
    staff=staffSerializers(source='staff_suuid',many=True,read_only=False)
    camera=cameraSerializers(source='camera_suuid',many=True,read_only=False)
    class Meta:
        model=store
        fields=['start_time','end_time','category','address','contact_id','staff','camera','tuuid','name']

class candidateSerializers(serializers.ModelSerializer):
    class Meta:
        model=candidate
        fields=['name','sex','age','height','skintone','clothing']

class eventpoolSerializers(serializers.ModelSerializer):
    candidate=candidateSerializers(source='eventpool_cauuid',many=True,read_only=False)
    camera=cameraSerializers(source='eventpool_cuuid',many=True,read_only=False)

    class Meta:
        model=eventpool
        fields=['start_time','end_time','candidate','camera','event_time','euuid','name','kind','tuuid','creation_time','last_modification_time']

class bbSerializers(serializers.ModelSerializer):
    

    class Meta:
        model=bb
        fields=['framecount','startx','starty','endx','endy']
