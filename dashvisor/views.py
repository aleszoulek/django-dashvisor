from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, Http404

from dashvisor.backends import backend

def dashboard(request):
    backend.refresh()
    return render_to_response(
        'dashvisor/dashboard.html',
        {
            'servers': backend.servers,
        }
    )

def control(request, server, process, action):
    print server, process, action
    if action not in ('start', 'stop', 'restart'):
        raise Http404

    getattr(backend.servers[server], action)(process)
    return HttpResponseRedirect('/') # TODO url reverse
