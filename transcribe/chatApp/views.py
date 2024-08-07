from django.shortcuts import render
from .models import Room, Message
from django.shortcuts import redirect
# from django.template.response import TemplateResponse


def CreateRoom(request):
    if request.method == 'POST':
        username = request.POST['username']
        room = request.POST['room']

        try:
            get_room = Room.objects.get(room_name=room)
        except Room.DoesNotExist:
            new_room = Room(room_name=room)
            new_room.save()
        return redirect('chatApp:room', room_name=room, username=username)


    return render(request, 'chatApp/index.html')


def MessageView(request, room_name, username):
    get_room = Room.objects.get(room_name=room_name)
    get_messages = Message.objects.filter(room=get_room)

    context = {
        'messages': get_messages,
        'user': username,
        'room_name': room_name,
    }

    return render(request, 'chatApp/message.html', context)

