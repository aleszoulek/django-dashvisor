from django.shortcuts import render_to_response

from dashvisor.backends import backend

def dashboard(request):
    return render_to_response(
        'dashvisor/dashboard.html',
        {'servers': backend.servers}
    )

