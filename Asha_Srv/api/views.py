from rest_framework.response import Response
from rest_framework.decorators import api_view

import requests
import json

from base.models import QueryLog, ErrorLog

from .serializers import *

from django.http import FileResponse, HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from pathlib import Path

import os

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

@api_view(["POST", "GET"])
def answer(request):
    print({"query":request.data["query"]})
    if request.data["query"] == "check1":
        return Response({'query': 'cervical cancer', 'answers': [{'answer': 'COPD', 'context': 'ypertension Diabetes Oral   Cancer  Breast   Cancer   Cervical   Cancer  COPD   (Respiratory   Disorders) \nCondition Date of   Diagnosis  Treatment In', 'offsets_in_document': {'start': 526, 'end': 530}, 'score': 0.06348967552185059, 'meta': {'name': 'asha_ncd-page-66.txt'}}, {'answer': 'Early age at first child birth. \nHigher numbers of pregnancy and childbirth', 'context': 'e. \nRisk Factors for Cervical Cancer \nEarly age at first child birth. \nHigher numbers of pregnancy and childbirth.  \nIn this Chapter,  you will learn ', 'offsets_in_document': {'start': 873, 'end': 948}, 'score': 0.03945968672633171, 'meta': {'name': 'asha_ncd-page-49.txt'}}, {'answer': 'Hypertension  Diabetes Oral   Cancer  Breast   Cancer   Cervical   Cancer  COPD   (Respiratory   Disorders) \nHypertension', 'context': '-    Remarks  \nHypertension  Diabetes Oral   Cancer  Breast   Cancer   Cervical   Cancer  COPD   (Respiratory   Disorders) \nHypertension Diabetes Oral', 'offsets_in_document': {'start': 343, 'end': 464}, 'score': 0.003709680400788784, 'meta': {'name': 'asha_ncd-page-66.txt'}}]})
    if request.data['query'] == "check2":
        return Response({'query': 'pregnancy', 'answers': [{'answer': 'Pregnancy is a natural event in the life of women of reproductive age   group', 'context': 'Pregnancy is a natural event in the life of women of reproductive age   group. However, during pregnancy and childbirth some problems may arise   whic', 'offsets_in_document': {'start': 0, 'end': 77}, 'score': 0.0326831191778183, 'meta': {'name': 'book-no-2-page-12.txt'}}, {'answer': 'where to deliver', 'context': 'ised proper nutrition,   rest, exercise. They can make plans about where to deliver. This will help   both the woman and baby to have a happy and heal', 'offsets_in_document': {'start': 634, 'end': 650}, 'score': 0.02641274593770504, 'meta': {'name': 'book-no-2-page-12.txt'}}, {'answer': 'â€', 'context': 'h in the CHC or City Hospital. \nDangers are present even during childbirthâ€”bleeding, retention of placenta  or lack of progress. \nSometimes placenta', 'offsets_in_document': {'start': 158, 'end': 160}, 'score': 0.023338977247476578, 'meta': {'name': 'book-no-1-page-77.txt'}}, {'answer': 'nursedidi', 'context': 'poor sections of community. \nEncourage women to follow advice given by nursedidi during pregnancy  check ups. \nEvery women need to undergo four checku', 'offsets_in_document': {'start': 1012, 'end': 1021}, 'score': 0.007620692253112793, 'meta': {'name': 'book-no-1-page-77.txt'}}]})
    x = requests.post("http://127.0.0.1:7000/check/", json = request.data)
    print(x.json())
    log = QueryLog()
    # log.query_text = request.data["query"]
    # log.answer_text = x.text
    # log.imageResponse = False
    try:
        log.enterData(
            query_text=request.data["query"], 
            answer_text=x.text, 
            imageResponse=False, 
            user=request.data["user"]
        )
    except:
        log.enterData(
            query_text=request.data["query"], 
            answer_text=x.text, 
            imageResponse=False, 
            user=""
        )
    finally:
        log.save()
    return Response(x.json())

@api_view(["GET","POST"])
def reportError(request):
    print("error received")
    err = ErrorLog()
    try:
        err.enterData(
            error_text=request.data["error"], 
            user=request.data["user"]
        )
    except:
        err.enterData(
            error_text=request.data["error"], user=""
        )
    finally:
        err.save()
    return Response({"message":"Error has been registered"})

class PdfFileView(APIView):
    def get(self, request, filename):
        
        response = FileResponse(open( os.getcwd() + f"/pdf_files/{filename}",'rb'))
        response['Content-Disposition'] = f'inline; filename="{filename}"'
        
        return response