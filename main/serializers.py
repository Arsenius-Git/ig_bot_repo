from rest_framework import serializers
from .models import IgModel

class IgSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='message-detail'
    )
    class Meta:
        model = IgModel
        fields = ['url', 'id', 'message', 'sender']
