from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from SearchEngine.Searching.QueryRetreival import QueryRetrieval

query_retrieval = QueryRetrieval()

@csrf_exempt
def index(request):
    return render(request, "index.html")


@csrf_exempt
def basic_search(request):
    query = request.POST.get("query")
    query_retrieval.adv_query(query, 30)
    return render(request, "adv_search.html")


@csrf_exempt
def adv_search(request):
    # indexReader
    nct_id = request.POST.get("nct_id")
    fields_list = ["official_title", "breif_summary", "criteia", "detailed_description"]
    search_string = {}
    for field in fields_list:
        field_query_string = request.POST.get(field)
        if field_query_string is not None and len(field_query_string) != 0:
            search_string[field] = field_query_string

    query_retrieval.adv_query(search_string, 30)
    return render(request, "adv_search.html")



@csrf_exempt
def search(request):
    # indexReader
    print("request.body",request.body)
    body_unicode = request.body
    body = json.loads(body_unicode)
    searchItem = body['searchItem']

    query = searchItem
   
    return_res = {}
    res = query_retrieval.search(query, 30)

    return_res["success"] = True
    return_res["docs"] = res
    print(res)
    return JsonResponse(return_res)

@csrf_exempt
def getdoc(request):
    query = request.POST.get("docid")
    # TODO return value
    # If true
    doc = {"title": "emergency room",
           "contents": ["A 31-year-old woman with no previous medical problems comes \
                        to the emergency room with a history of 2 weeks of joint pain \
                        and fatigue.",
                        "called if the Promise is rejected. This function has one argument, \
                        the rejection reason. If it is not a function, it is internally replaced with a \
                          function (it throws an error it received as argument)"
                        ]
           }
    return JsonResponse(doc)


