from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User


def get_all_users_data(request):
    user_list = User.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'user_list': user_list,
    }
    return HttpResponse(template.render(context, request))
