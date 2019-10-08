from rest_framework import serializers

from . import models

class MemberSerializer(serializers.ModelSerializer):
    """
        微信成员
    """

    class Meta:
        model = models.Member
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    """
        订单
    """
    # order_number = serializers.SerializerMethodField()

    class Meta:
        model = models.Order
        fields = '__all__'
        deepth = 1

    # def get_order_number(self, order):
        # return union.order_number()

class DoneSerializer(serializers.ModelSerializer):
    """
        订单完成记录
    """

    class Meta:
        model = models.Done
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    """
        活动
    """

    class Meta:
        model = models.Activity
        fields = '__all__'