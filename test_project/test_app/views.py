from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.sessions.models import Session

def index(request):
    session = Session.objects.all().first()

    return render_to_response(
        'index.html',
        {'session_info': None if session is None else session.get_decoded()},
        context_instance=RequestContext(request)
    )
