from django.shortcuts import render
import requests
from django.http import JsonResponse
# Create your views here.


def HomeView(request):
    if request.method == 'POST':
        country = request.POST.get('country')
    
   
    
        url = "https://covid-193.p.rapidapi.com/statistics"
        query_string = {'country':country}
        headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "1a270bb839mshd4dcf5cc00d2b7ap113189jsn4cbb99d1f6bd"
        }
        data = requests.request("GET", url, headers=headers,params=query_string).json()
        data = data['response']
        return JsonResponse(data,safe=False)
    

    return render(request,'index.html')