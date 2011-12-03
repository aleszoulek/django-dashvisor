from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.utils import simplejson

from dashvisor.backends import backend

def dashboard(request):
    backend.refresh()
    return render_to_response(
        'dashvisor/dashboard.html',
        {
            'servers': backend.servers,
            'query_url': reverse('dashvisor_query'),
            'constants': {
                'stopped': 0,
                'running': 20,
            },
        }
    )

def control(request, server, process, action):
    print server, process, action
    if action not in ('start', 'stop', 'restart'):
        raise Http404

    getattr(backend.servers[server], action)(process)
    return HttpResponseRedirect('/') # TODO url reverse

def query(request):
    id = request.GET['server']
    server = backend.servers[id]
    action = request.GET['action']
    response_dict = {}
    if action == 'refresh':
        server.refresh()
        response_dict['status'] = server.status.values()
        response_dict['status'].sort(key=lambda x: (x['group'], x['name']))
        response_dict['server'] = {'name': server.name, 'id': id}

    print response_dict
    return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')
