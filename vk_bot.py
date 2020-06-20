import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from Auth import vk_api_auth_community, vk_api_auth_service
from urllib.parse import urlparse
import json

# отправка сообщния
def write_msg(user_id, message, keyboard):
    vk_api_auth_community.method('messages.send',
                                 {'user_id': user_id,
                                  'message': message,
                                  'random_id': vk_api.utils.get_random_id(),
                                  'keyboard': json.dumps(keyboard)})


# класс комманд
class Commands:
    community = "сообщества:"


class Answer:
    success_comm = "Сообщества добавлены успешно!\n"
    wrong_comm = "Не могу разобрать адреса сообществ, попробуй еще раз!\n"
    choose_category_location = "Выбери категории, которые ты хочешь отслеживать и локацию! Как закончишь добвлять категории, нажми на кнопку 'Закончить'"
    standard = "Приветствую! Это ФудБот, который поможет тебе получать уведомления об объявлениях в фудшеринговых сообществах! \n Для начала отправь список сообществ через запятую, из которых хочешь получать объявления со словом 'сообщества:' и двоеточием в начале сообщения. \n Пример: сообщества: https://vk.com/murmewmur, https://vk.com/public196448452 \n"


# список сообществ юзера
listComm = []


# парсинг сообщения от пользователя с сообществами
def get_communities_from_request(str):
    if str.split(Commands.community)[1]:
        list_comm = str.split(Commands.community)[1].split(",")
        if len(list_comm) > 0:
            return list_comm
        else:
            return []
    else:
        return []


# Добавление сообществ
def add_communities_user(request):
    list_communities = []
    if len(get_communities_from_request(request)) > 0:
        for comm in get_communities_from_request(request):
            list_communities.append(comm)
            # тут надо схранять в бд
            print(list_communities)
        write_msg(event.user_id, Answer.success_comm + Answer.choose_category_location,
                  {"buttons": [[
                      {
                          "action": {
                              "type": "location",
                              "payload": "{\"button\": \"1\"}"
                          }
                      }
                  ],
                      [
                          {
                              "action": {
                                  "type": "text",
                                  "payload": "{\"button\": \"0\"}",
                                  "label": "ЗАКОНЧИТЬ"
                              },
                              "color": "positive"
                          }],
                [
                    {
                        "action": {
                            "type": "text",
                            "payload": "{\"button\": \"2\"}",
                            "label": "Фрукты"
                        },
                        "color": "primary"
                    }],
                    [{
                        "action": {
                            "type": "text",
                            "payload": "{\"button\": \"3\"}",
                            "label": "Овощи"
                        },
                        "color": "primary"
                    }],
                    [{
                        "action": {
                            "type": "text",
                            "payload": "{\"button\": \"4\"}",
                            "label": "Крупы"
                        },
                        "color": "primary"
                    }
                ]], "one_time": False})
    else:
        write_msg(event.user_id, Answer.wrong_comm, {})
        write_msg(event.user_id, Answer.standard, {})
    return list_communities


# Работа с сообщениями
longpoll = VkLongPoll(vk_api_auth_community)

# Основной цикл
for event in longpoll.listen():
    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:

        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:

            # Сообщение от пользователя
            request = event.text.lower()

            # Каменная логика ответа
            if request.startswith(Commands.community):
                add_communities_user(request)
            else:
                write_msg(event.user_id, Answer.standard, {})


# функция обрезания url группы, чтобы остался только идентификатор или короткое имя
def format_group_url(group_url):
    # обрезаем все что до слэша справа нпрмр https://vk.com/murmewmur' станет murmewmur
    short_name = urlparse(group_url).path.split('/')[1]
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

# # тестируемая группа
# url = "https://vk.com/murmewmur"
# # короткое имя
# name_group = format_group_url(url)
# # получаем пост по короткому имени сообщества
# get_post(name_group)
