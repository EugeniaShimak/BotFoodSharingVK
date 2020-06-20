import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from Auth import vk_api_auth_community, vk_api_auth_service
from urllib.parse import urlparse


# отправка сообщния
def write_msg(user_id, message):
    vk_api_auth_community.method('messages.send',
    {'user_id': user_id, 'message': message, 'random_id': vk_api.utils.get_random_id()})


# Работа с сообщениями
longpoll = VkLongPoll(vk_api_auth_community)


# класс комманд
class Commands:
    hi = ["привет"]
    by = ["пока"]

# Основной цикл
    for event in longpoll.listen():

        # Если пришло новое сообщение
        if event.type == VkEventType.MESSAGE_NEW:

            # Если оно имеет метку для меня( то есть бота)
            if event.to_me:

                # Сообщение от пользователя
                request = event.text

                # Каменная логика ответа
                if request == "привет":
                    write_msg(event.user_id, "Хай")
                elif request == "пока":
                    write_msg(event.user_id, "Пока((")
                else:
                    write_msg(event.user_id, "Не поняла вашего ответа...")


# функция обрезания url группы, чтобы остался только идентификатор или короткое имя
def format_group_url(group_url):
    short_name = urlparse(group_url).path.split('/')[1]  # обрезаем все что до слэша справа нпрмр https://vk.com/murmewmur' станет murmewmur
    print(short_name)
    return short_name


# функция возвращает  id группы, принимает в себя короткое имя группы или идентификатор
def get_group_id(group_name):
    data_group = vk_api_auth_service.groups.getById(group_id=group_name, v=5.92)
    print(data_group)
    return data_group[0]['id']


# функция возвращает  последний пост группы, принимает в себя короткое имя группы или идентификатор
def get_post(group_name):
    group_id = str(get_group_id(group_name))
    print("group_id" + group_id)
    data_wall = vk_api_auth_service.wall.get(owner_id="-" + str(group_id), domain=group_name, count=1, v=5.92)
    print("data_wall" + str(data_wall))
    for post in data_wall:
        print("post" + str(post))
        return post


# тестируемая группа
url = "https://vk.com/murmewmur"
# короткое имя
name_group = format_group_url(url)
# получаем пост по короткому имени сообщества
get_post(name_group)

