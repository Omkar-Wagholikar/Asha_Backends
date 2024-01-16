from rest_framework.response import Response
from rest_framework.decorators import api_view

from base.models import QueryLog
from .serializers import QuerySerializer
from .QueryModel import QueryModel

q = QueryModel()
# print(q.query("are you working?"))

@api_view(['GET'])
def getData(request):
    items = QueryLog.objects.all()

    serial = QuerySerializer(items, many = True)
    return Response(serial.data)

@api_view(["POST"])
def addQuery(request):
    serial = QuerySerializer(data = request.data)
    if serial.is_valid():
        serial.save()
    else:
        return Response({"Status":"error"})
    return Response({"Status":"Success"})

@api_view(["POST"])
def check(request):
    temp = request.data
    res = str(temp)
    print("-->",res)  
    res = q.query(temp["query"])
    return Response(res)
