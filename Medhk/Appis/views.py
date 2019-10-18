import uuid
import json
import requests

from django_filters.rest_framework.backends import DjangoFilterBackend

from rest_framework import filters, pagination
from rest_framework import mixins, viewsets, views, status
from rest_framework.response import Response
from rest_framework.decorators import list_route
from django.forms.models import model_to_dict

from Appis import models
from Appis import serializers
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# View
class MemberViewSet(viewsets.ModelViewSet):
    """
        微信会员
    """
    queryset = models.Member.objects.all()
    serializer_class = serializers.MemberSerializer

    @list_route (methods = ['post'])
    def login (self, request):
        data = json.loads(request.body)
        code = data['code']
        appid = data['appid']
        secret = data['secret']
        user_info = data['userInfo']
        res = {
            'openid': 'xxx',
        }
        data = user_info
        
        url = 'https://api.weixin.qq.com/sns/jscode2session?appid='+ appid +'&secret='+ secret +'&js_code='+ code +'&grant_type=authorization_code'
        req = requests.post(url, data = {})
        openid = eval(req.text)['openid']
        
        member = models.Member.objects.filter(openid = openid)
        if len(member):
            member = model_to_dict(member[0])
        try:
            data['openid'] = openid
            member, is_new = models.Member.objects.get_or_create(**data)
            print('-------------------------')
            print(member, is_new)
        except err: 
            print('err =', err)
        res['openid'] = openid
        res['id'] = member.id
        return Response(res)
        
    """
    @list_route (methods = ['post'])
    def login (self, request):
        is_new = True
        data = json.loads(request.body)
        user = models.Member.objects.filter(username = data['username'])
        if len(user):
            is_new = False
        else:
            user = models.Member.objects.create(**data)
            user = models.Member.objects.filter(username = data['username'])
        return Response(res)
    """

class OrderViewSet(viewsets.ModelViewSet):
    """
        订单
    """
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ('status', )
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = ('id', )