from datetime import datetime
from itertools import chain
from chat.models import PrivateChatRoom,RoomChatMessage
from django.contrib.humanize.templatetags.humanize import naturalday
from django.core.serializers.python import Serializer

from scientistSite.settings import SITE_NAME




def find_or_create_private_chat(user1, user2):
	try:
		chat = PrivateChatRoom.objects.get(user1=user1, user2=user2)
	except PrivateChatRoom.DoesNotExist:
		try:
			chat = PrivateChatRoom.objects.get(user1=user2, user2=user1)
		except PrivateChatRoom.DoesNotExist:
			chat = PrivateChatRoom(user1=user1, user2=user2)
			chat.save()
	return chat


def calculate_timestamp(timestamp):
	"""
	1. Today or yesterday:
		- EX: 'today at 10:56 AM'
		- EX: 'yesterday at 5:19 PM'
	2. other:
		- EX: 05/06/2020
		- EX: 12/28/2020
	"""
	ts = ""
	# Today or yesterday
	if str((naturalday(timestamp)) == "сегодня") or str((naturalday(timestamp)) == "вчера"):
		str_time = datetime.strftime(timestamp, "%I:%M")
		str_time = str_time.strip("0")
		ts = f"{naturalday(timestamp)} at {str_time}"
	# other days
	else:
		str_time = datetime.strftime(timestamp, "%d/%m/%Y")
		ts = f"{str_time}"
	return str(ts)


"""
Аналог сериализтора для выдачи сообщений
"""

class LazyRoomChatMessageEncoder(Serializer):
    def get_dump_object(self, obj):
        dump_object = {}
        dump_object.update({'msg_id': str(obj.id)})
        dump_object.update({'user_id': str(obj.user.id)})
        dump_object.update({'username': str(obj.user.name)})
        dump_object.update({'message': str(obj.content)})
        dump_object.update({'profile_image': SITE_NAME+str(obj.user.image.url)})
        dump_object.update({'natural_timestamp': str(obj.timestamp)})
        return dump_object

def get_room_list(user):

    #rooms1 = list(PrivateChatRoom.objects.filter(user1=user, is_active = True))
    #rooms2 = list (PrivateChatRoom.objects.filter(user2=user, is_active = True))
    #rooms = rooms1
    #rooms.append(rooms2)
    #print(rooms)
    mes_and_f = []
    try:
        rooms1 = PrivateChatRoom.objects.filter(user1=user, is_active=True)
        rooms2 = PrivateChatRoom.objects.filter(user2=user, is_active=True)
        rooms = list(chain(rooms1, rooms2))
    except:
        return mes_and_f
    if rooms:
        for room in rooms:
            if str(room.user1) == str(user):
                friend = room.user2
            else:
                friend = room.user1
            mes = RoomChatMessage.objects.get_mes_by_room(room)
            if mes:
                print("mes:",mes)
                mes_and_f.append({
                    'command':'get_list',
                    'friend_id':friend.id,
                    "friend_photo":SITE_NAME+str(friend.image.url),
                    "friend_name":friend.name,
                    "friend_surname": friend.surname,
                    "room_id": room.pk,
                    "last_message": mes.content,
                    "timestamp": str(mes.timestamp),
                    "mes_id": mes.pk
                })
            else:
                mes_and_f.append({
                    'command': 'get_list',
                    'friend_id': friend.id,
                    "friend_photo": SITE_NAME + str(friend.image.url),
                    "friend_name": friend.name,
                    "friend_surname": friend.surname,
                    "room_id": room.pk,
                    "last_message": "Нет сообщений"
                })

    return mes_and_f