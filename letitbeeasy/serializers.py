from rest_framework import serializers
from letitbeeasy.models import Content, LANGUAGE_CHOICES, STYLE_CHOICES, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'position', 'department' , 'contact' ,'user_details']
class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'tosent', 'position', 'subject', 'matter', 'author','key']