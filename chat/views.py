from django.shortcuts import render
from django.views import View
from user_auth.models import *

class Chat(View):
    def get(self, request, username):
        curr_user = User.objects.get(username=request.user.username)
        chat_user = User.objects.get(username=username)
        curr_room = Room.objects.filter(users=chat_user).intersection(Room.objects.filter(users=curr_user))
        if not curr_room:
            curr_room = Room.objects.create(name=f"{curr_user}_{chat_user}")
            curr_room.users.add(chat_user)
            curr_room.users.add(curr_user)
            msgs = Message.objects.filter(room=curr_room)
            return render(request, "chat/chat.html", {"user":chat_user, "room":curr_room, "msgs":msgs})
        curr_room = curr_room[0]
        msgs = Message.objects.filter(room=curr_room)
        return render(request, "chat/chat.html", {"user":chat_user, "room":curr_room, "msgs":msgs})

