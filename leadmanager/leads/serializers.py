# use serializer to change model to json format 
from rest_framework import serializers
from leads.models import Lead 

# create serializer 
# to change lead model to serializer 

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead 
        fields = '__all__'
