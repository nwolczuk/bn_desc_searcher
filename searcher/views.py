from django.db.models.fields import DecimalField
from django.shortcuts import render, redirect
from django.db.models.functions import Length

from .models import Descriptors, Corporatives

# Create your views here.
def home(request):
    if request.method == 'POST':
        search_query = request.POST['search_query']
        if search_query.startswith('!'):
            results = Descriptors.objects.filter(descriptor__icontains=search_query[1:])
        else:
            search_list = search_query.split('&')
            regex_pattern = '^' + search_list[0] + '|\$.' + search_list[0] + '| ' + search_list[0]
            q = Descriptors.objects.filter(descriptor__iregex=regex_pattern)
            if len(search_list) > 1:
                for phrase in search_list[1:]:
                    regex_pattern = '^' + phrase + '|\$.' + phrase + '| ' + phrase
                    q = q.filter(descriptor__iregex=regex_pattern)
            results = q  
        return render(request, 'searcher/result.html', {'search_query': search_query, 'results': results})
    else: 
        return render(request, 'searcher/base.html')

def corporatives(request):
    if request.method == 'POST':
        search_query = request.POST['search_query']
        if search_query.startswith('!'):
            results = Corporatives.objects.filter(corporative__icontains=search_query[1:]).order_by(Length('corporative'))
        else:
            search_list = search_query.split('&')
            regex_pattern = '^' + search_list[0] + '|\$.' + search_list[0] + '| ' + search_list[0]
            q = Corporatives.objects.filter(corporative__iregex=regex_pattern)
            if len(search_list) > 1:
                for phrase in search_list[1:]:
                    regex_pattern = '^' + phrase + '|\$.' + phrase + '| ' + phrase
                    q = q.filter(corporative__iregex=regex_pattern)
            results = q.order_by(Length('corporative'))
        return render(request, 'searcher/corporativesresults.html', {'search_query': search_query, 'results': results})
    else: 
        return render(request, 'searcher/corporativesbase.html')


def mainredirect(request):
    return redirect('/home/')