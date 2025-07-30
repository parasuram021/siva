from django.shortcuts import render

def friend1_chat(request):
    return render(request, 'chatapp/friend1_chat.html', {'room_name': 'friend1_friend2'})

def friend2_chat(request):
    return render(request, 'chatapp/friend2_chat.html', {'room_name': 'friend1_friend2'})
