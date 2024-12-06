from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    if request.method == "POST":
        text = request.POST.get('text', '')
        title = request.POST.get('title', '')
       # utfTtile = title.decode()
        # Сохраняем данные в куках
        response = HttpResponse("Данные сохранены!")
        response.set_cookie('text', text)  # Сохраняем текст напрямую
        response.set_cookie('title', title)  # Сохраняем заголовок напрямую
        
        return response
    
    # Получаем данные из кук
    text_from_cookies = request.COOKIES.get('text', '')
    title_from_cookies = request.COOKIES.get('title', '')

    context = {
        'text': text_from_cookies,
        'title': title_from_cookies,
    }

    return render(request, 'app/index.html', context)