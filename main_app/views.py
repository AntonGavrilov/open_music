from django.shortcuts import get_object_or_404,render
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request,'main_app/index.html')

# def user_index(request, current_id_user):
#     return render(request, 'music_library_app/duser.html')