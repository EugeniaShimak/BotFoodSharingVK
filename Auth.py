import vk_api
from vk_api import VkApi

from Config import tokenCommunity, tokenService
import vk

# Авторизация как сообщество
vk_api_auth_community: VkApi = vk_api.VkApi(token=tokenCommunity)


# Авторизация через сервисный токен
session = vk.Session(access_token=tokenService)
vk_api_auth_service = vk.API(session)
