# Create your views here.
from django.http import HttpResponse, JsonResponse
from drf_spectacular.utils import extend_schema

from rest_framework.decorators import api_view
from stock.serializer import StockSerializer
from django.http import StreamingHttpResponse
from django.views.decorators.http import require_http_methods
import asyncio
import random
import json


@extend_schema(request=StockSerializer, responses={})
@api_view(["GET"])
def ohlc(request):
    return JsonResponse({"value": "$5000"})


@require_http_methods(["GET", "OPTIONS"])
async def sse(request):
    async def iterator():
        while True:
            val = round(random.random() * 1000, 2)
            stock_update = {
                "stock_id": "aapl",
                "price": val,
                "volume": 1000,
            }
            yield f"data: {json.dumps(stock_update)}\n\n"
            await asyncio.sleep(0.5)

    response = StreamingHttpResponse(
        streaming_content=iterator(), content_type="text/event-stream"
    )
    response["Cache-Control"] = "no-cache"
    response["Connection"] = "keep-alive"
    response["Content-Encoding"] = "text/event-stream"
    return response


async def sse_stream(request):
    """
    Sends server-sent events to the client.
    """

    async def event_stream():
        emojis = ["🚀", "🐎", "🌅", "🦾", "🍇"]
        i = 0
        while True:
            yield f"data: {random.choice(emojis)} {i}\n\n"
            i += 1
            await asyncio.sleep(1)

    return StreamingHttpResponse(event_stream(), content_type="text/event-stream")
