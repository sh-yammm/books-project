from rest_framework import serializers

from .models import Books

class BookSerializer(serializers.ModelSerializer):

    class Meta:

        model = Books

        fields = '__all__'     # to include all fields in the model 

        # exclude =['active_status','uuid'] 

        read_only_fields = ['active_status','uuid']  # to make fields read-only 