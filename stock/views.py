# Create your views here.
from django.http import HttpResponse, JsonResponse
from drf_spectacular.utils import extend_schema

from rest_framework.decorators import api_view
from stock.serializer import StockSerializer


@extend_schema(request=StockSerializer, responses={})
@api_view(["GET"])
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@extend_schema(request=StockSerializer, responses={})
@api_view(["GET"])
def ohlc(request):
    return JsonResponse({"value": "$5000"})
