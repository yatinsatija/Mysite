from django.db import models
import uuid
from django.utils.timezone import now
from phone_field import PhoneField
 

class base(models.Model):
    name=models.CharField(max_length=100)
    creation_time=models.DateTimeField(auto_now_add=True)
    last_modification_time=models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class tenant(base):
    tuuid= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
class store(base):
    suuid= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tuuid=models.ForeignKey(tenant, on_delete = models.CASCADE)
    map_id=models.CharField(max_length=100,blank=False)
    address=models.CharField(max_length=200,blank=False)
    start_time=models.DateTimeField(max_length=50, blank=False)
    end_time=models.DateTimeField(max_length=50,blank=False)
    choices=(
        ('GROCERY','GROCERIES'),
        ('MEDICAL','MEDICINE'),
        ('APPARELS','APPARELS'),
        ('ELECTRONICS','ELECTRONICS'),
        ('WHOLESALE','WHOLESALE'),
        ('SUPERMARKET','SUPERMARKET'),
        ('AUTOMOBILE','AUTOMOBILE'),
        ('ENTERTAINMENT AND ARTS','ENTERTAINMENT AND ARTS'),
        ('HEALTH AND BEAUTY','HEALTH AND BEAUTY'),
        ('FOOD','FOOD'),
        ('TRAVEL','TRAVEL'),
        ('SPORTS','SPORTS')
    )
    category=models.CharField(max_length=50,choices=choices,blank=False)
    contact_id=PhoneField(max_length=50,blank=False,help_text='Contact phone number')
    

class staff(base):
    stuuid= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    suuid=models.ForeignKey(store,related_name='staff_suuid',on_delete = models.CASCADE)
    contact_number=PhoneField(max_length=50,blank=False,help_text='Contact phone number')
    choices=(
        ('MALE','MALE'),
        ('FEMALE','FEMALE'),
        ('OTHERS','OTHERS')
    )
    sex=models.CharField(max_length=10,blank=False,choices=choices)
    age=models.IntegerField(blank=False)
    option=(
        ('MANAGER','MANAGER'),
        ('ASSISTANT MANAGER','ASSISTANT MANAGER'),
        ('CASHIER','CASHIER'),
        ('CUSTOMER SERVICE REPRESENTATIVE','CUSTOMER SERVICE REPRESENTATIVE'),
        ('TRAINEE','TRAINEE'),
        ('SECURITY','SECURITY'),
        ('CLEANING','CLEANING')
    )
    
    designation=models.CharField(max_length=50,choices=option,blank=False)
class camera(base):
    cuuid= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    suuid=models.ForeignKey(store,related_name='camera_suuid',on_delete = models.CASCADE)
    model=models.CharField(max_length=100,blank=True)
    location=models.CharField(max_length=100,blank=True)

class candidate(models.Model):
    cauuid= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    suuid=models.ForeignKey(store,related_name='candidate_suuid',on_delete = models.CASCADE)

    name=models.CharField(max_length=100,blank=False)
    choices=(
        ('MALE','MALE'),
        ('FEMALE','FEMALE'),
        ('OTHERS','OTHERS')
    )
    sex=models.CharField(max_length=10,blank=False,choices=choices)
    age=models.IntegerField(blank=False)
    height=models.IntegerField(blank=False)
    c=(
        ('UNDERTONE','UNDERTONE'),
        ('COOLTONE','COOLTONE'),
        ('WARMTONE','WARMTONE'),
        ('OTHERS','OTHERS')
    )
    skintone=models.CharField(max_length=40,blank=False,choices=c)
    clothing=models.CharField(max_length=100,blank=False)

class eventpool(base):
    euuid= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    start_time=models.DateTimeField(max_length=50, blank=False)
    end_time=models.DateTimeField(max_length=50,blank=False)
    ty=(
        ('IN','IN'),
        ('OUT','OUT'),
        ('STANDING','STANDING'),
        ('OTHERS','OTHERS')
    )
    type=models.CharField(max_length=40,blank=False,choices=ty)
    cauuid=models.ForeignKey(candidate,related_name='eventpool_cauuid',on_delete = models.CASCADE)
    cuuid=models.ForeignKey(camera,related_name='eventpool_cuuid',on_delete = models.CASCADE)
    event_time=models.DateTimeField(max_length=50, blank=False)
    tuuid=models.ForeignKey(tenant, on_delete = models.CASCADE)
    kind=models.CharField(max_length=30,default='eventpool')

class summary(models.Model):
    smuuid= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    total_in=models.IntegerField(blank=False)
    total_out=models.IntegerField(blank=False)
    peak=models.IntegerField(blank=False)
    
class bb(models.Model):
    framecount=models.CharField(max_length=40,blank=False)
    startx=models.CharField(max_length=40,blank=False)
    starty=models.CharField(max_length=40,blank=False)
    endx=models.CharField(max_length=40,blank=False)
    endy=models.CharField(max_length=40,blank=False)
    in_time = models.DateTimeField('in timing')








    




