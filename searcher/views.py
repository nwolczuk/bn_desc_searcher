from django.db.models.fields import DecimalField
from django.shortcuts import render

from .models import Descriptors

# Create your views here.
def home(request):
    if request.method == 'POST':
        search_query = request.POST['search_query']
        if search_query.startswith('any:'):
            results = Descriptors.objects.filter(descriptor__contains=search_query[4:].lower())
        else:
            regex_pattern = '^' + search_query.capitalize() + '|^' + search_query.lower() + '|\$.' + search_query.lower() + '|\$.' + search_query.capitalize() + '| ' + search_query.capitalize() + '| ' + search_query.lower()
            results = Descriptors.objects.filter(descriptor__regex=regex_pattern)
        return render(request, 'searcher/result.html', {'search_query': search_query, 'results': results})
    else: 
        return render(request, 'searcher/base.html')