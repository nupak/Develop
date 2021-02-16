from django.db import models
from django.conf import settings
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .utils import get_room_list
from django.db.models.signals import post_save
from django.dispatch import receiver

class PrivateChatRoom(models.Model):

    """
    Приватный чат между 2 пользователями
    """

    user1            = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name='user1')
    user2            = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name='user2')
    is_active        = models.BooleanField(default=True)

    def __str__(self):
        return f"Чат между {self.user1} и {self.user2}"

    @property
    def group_name(self):
        """
        Возвращает имя канала, на который сокеты должны
        подписаться, чтобы они отправляли сообщение по мере их создания
        """
        return f"PrivateChatRoom-{self.id}"


class RoomChatMessageManager(models.Manager):
    def by_room(self,room):
        try:
            qs = RoomChatMessage.objects.filter(room__id=room.id).order_by('-timestamp')
        except:
            qs=[]
        return qs

    def get_mes_by_room(self, room):
        try:
            qs = RoomChatMessage.objects.filter(room__id=room.id).order_by('-timestamp')[0]
        except IndexError:
            qs=[]
        return qs


class RoomChatMessage(models.Model):
    '''
    Сообщения чата
    '''
    user        =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room        =models.ForeignKey(PrivateChatRoom,on_delete=models.CASCADE)
    timestamp   =models.DateTimeField(auto_now_add=True)
    content     =models.TextField(unique=False,blank=False)

    objects = RoomChatMessageManager()

    def __str__(self):
        return  self.content


def send_chat_message(data, channel_name):
    async_to_sync(get_channel_layer().group_send)(channel_name, data)


@receiver(post_save,sender = RoomChatMessage,)

def new_message(sender, instance, created, **kwargs):

    user_1= PrivateChatRoom.objects.get(ins=instance.room).user1
    user_2= PrivateChatRoom.objects.get(rom=instance.room).user2
    channel_name_1 = f"Listroom-{user_1}"
    channel_name_2 = f"Listroom-{user_2}"
    data_1 = get_room_list(user_1)
    data_2 = get_room_list(user_2)
    send_chat_message(data_1, channel_name_1)
    send_chat_message(data_2, channel_name_2)
    print(data_1,data_2)

#post_save.connect(new_message, sender=RoomChatMessage, dispatch_uid='new_group_message')