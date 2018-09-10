from rest_framework import serializers
from touchpoint.models import Touchpoint
 
class TouchpointSerializer(serializers.HyperlinkedModelSerializer):
    #touchpoint = serializers.ReadOnlyField(source='touchpoint.username')
 
    class Meta:
        model = Touchpoint
        fields = ('username','status', 'modified_date')
