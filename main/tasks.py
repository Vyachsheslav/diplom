from celery import Celery, shared_task
from django.http.response import JsonResponse
from rest_framework.response import Response

from users.serializers import UserSerializer
