# share/views.py
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from .models import SharedText
from django.utils import timezone

def generate_code():
    return get_random_string(4, '0123456789')

def submit_text(request):
    if request.method == 'POST':
        text = request.POST['text']
        code = generate_code()
        SharedText.objects.create(text=text, code=code)
        return render(request, 'share/success.html', {'code': code})
    return render(request, 'share/submit.html')

def retrieve_text(request):
    if request.method == 'POST':
        code = request.POST['code']
        try:
            shared_text = SharedText.objects.get(code=code)
            if shared_text.is_expired():
                shared_text.delete()
                return render(request, 'share/expired.html')
            return render(request, 'share/retrieve.html', {'text': shared_text.text})
        except SharedText.DoesNotExist:
            return render(request, 'share/not_found.html')
    return render(request, 'share/retrieve_form.html')
