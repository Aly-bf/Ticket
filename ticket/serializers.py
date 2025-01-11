from rest_framework import serializers
from .models import Ticket
from django.contrib.auth.models import User

class TicketSerializers(serializers.ModelSerializer):
    # user_name = serializers.SerializerMethodField()
    class Meta:
        model = Ticket
        fields = '__all__'

    # def get_user_name(self, obj):
    #     if obj.user:
    #         return obj.user.username
    #     return "No user assigned"