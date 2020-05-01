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
        # I think add `544332520` to config is good idea
        if event.object.message["from_id"] == 544332520:

            # Command `gg`
            # <description>
            if event.object.message["text"].lower() == "/gg":
                try:
                    time.sleep(2)
                    vk.messages.send(
                        peer_id=event.object.message["peer_id"],
                        message=config.FLOOD_MSG,
                        keyboard=keyboard.menu,
                        random_id=0
                    )
                except Exception:
                    time.sleep(5)
                    continue

            # Command `stop`
            # <description>
            if event.object.message["text"].lower() == "/stop":
                vk.messages.send(
                    peer_id=event.object.message["peer_id"],
                    message="[Process finished]",
                    keyboard=menu,
                    random_id=0
                )
