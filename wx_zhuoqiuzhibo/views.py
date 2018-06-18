from django.shortcuts import render

# Create your views here.

import hashlib
import json
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from django.views import View
from rest_framework.response import Response
from rest_framework import  status

from tools.mongo_operation import get_rank
from wechat.tasks import call_updaterank
import json
import logging
logger = logging.getLogger(__name__)

class SnkRank(APIView):
    def post(self, request):
        try:
            data = request.data
            print(data)
            print(type(data))  #dict
            call_updaterank.delay(data)  ## 异步更新排名
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            print(e)
            logger.error(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        data = get_rank()
        if data:
            return Response(data, status=status.HTTP_200_OK, content_type=json)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)


    # django默认开启csrf防护，这里使用@csrf_exempt去掉防护
    # @csrf_exempt
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(SnkRank, self).dispatch(*args, **kwargs)