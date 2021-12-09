from django.shortcuts import render
from allauth.account.decorators import verified_email_required

@verified_email_required
def oauth_view(request):
    return render(request, '../templates/oauth.html', {})
