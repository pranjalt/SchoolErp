'''
Created on 15-Jan-2016

@author: Administrator
'''
from rest_framework import serializers
from SchoolERP.models import Sections, School,Class,BatchClasses


class BatchClassesSerializers(serializers.ModelSerializer):
    className = serializers.CharField(source='class_field.class_field',read_only=True)
    class Meta:
        model = BatchClasses
        fields = ('className',)