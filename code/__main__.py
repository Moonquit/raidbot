# -*- coding: utf8 -*-
import time

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

import config
import keyboard


# API and LP settings
vk = vk_api.VkApi(
    token=config.TOKEN,
    api_version=config.VERSION
)
longpoll = VkBotLongPoll(vk, config.GROUP_ID)
vk = vk.get_api()


# Main loop
for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:

            # if the bot was added to the chat       
            if event.from_chat:
                try:
                    #infinity cycle
                    while 1:
                        vk.messages.send(
                            chat_id = event.chat_id,
                            message=config.FLOOD_MSG,
                            keyboard=keyboard.menu,
                            random_id=0
                        )
                except Exception:
                    time.sleep(5)
                    continue


