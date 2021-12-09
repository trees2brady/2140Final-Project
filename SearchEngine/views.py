import json

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from SearchEngine.Searching.QueryRetreival import QueryRetrieval
from SearchEngine.Searching.QueryWithBERT import QueryWithBERT

query_retrieval = QueryRetrieval()
query_with_bert = QueryWithBERT()

@csrf_exempt
def index(request):
    return render(request, "index.html")


@csrf_exempt
def basic_search(request):
    query = request.POST.get("query")
    query_retrieval.adv_query(query, 30)
    return render(request, "adv_search.html")


@csrf_exempt
def search(request):
    # indexReader
    print("request.body", request.body)
    body_unicode = request.body
    body = json.loads(body_unicode)
    searchItem = body['searchItem']
    query = searchItem

    return_res = {}
    res = query_retrieval.search(query, 10)
    return_res["success"] = True
    return_res["docs"] = []
    return_res["docs"].append(res)
    query_with_bert.preprocess(query)
    bert_res = query_with_bert.encoderRank()
    return_res["docs"][0].extend(bert_res)
    print(res)
    return JsonResponse(return_res)


@csrf_exempt
def getdoc(request):
    docId = json.loads(request.body)["docid"]
    res = {}
    try:
        res = query_retrieval.read_original_file(docId, summary=False)
        if res["title"] == "":
            res = query_with_bert.getById(docId)
    except Exception as e:
        print("execute before using bert query")
        print("execute after using bert query")
    return JsonResponse(res)
