from django.shortcuts import render
import  requests

# Create your views here.

def index(request):
    data = True
    result = None
    globalSummary = None
    countries = None;
    while(data):
        try:
            result = requests.get('https://api.covid19api.com/summary')
            json = result.json()
           
            

            globalSummary = json['Global']
            countries = json['Countries']

            data = False
        except:
            data = True
    return render(request , 'index.html' ,
                  {'globalSummary' : globalSummary ,
                   'countries' : countries})


def nepal(request):
     result = requests.get('https://covid19.mohp.gov.np/covid/api/confirmedcases?fbclid=IwAR3hnWbCv_vSsuyAJChr_WhxUul4eACxnziA5zvqquyZY4wAO0-Z3O41hEg').json()
     nepal = result['nepal']
     return render(request , 'nepal.html' ,
                  {'nepal':nepal})

