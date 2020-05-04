from rest_framework_json_api import serializers
from order_transfer.models import Order

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('ordertext', 'amount')