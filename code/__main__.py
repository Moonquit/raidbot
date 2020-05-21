import asyncio
import re

import vk_dev

import config
import keyboard
import preview



api = vk_dev.Api(
    token=config.TOKEN,
    group_id=config.GROUP_ID,
    v=config.VERSION
)


lp = api >> vk_dev.LongPoll()

chats = 0

@lp.message_new()

async def flood(event, pl):
    """
    Flood if it was invited
    """
    global chats

    if (
        'action' in event.object.message and
        event.object.message.action.type == 'chat_invite_user'
    ):
        chats += 1
        print(f'\033[35m[*]\033[0m New chat | Total chats: {chats}')

        while True:
            try:
                await api.messages.send(
                    peer_id=event.object.message.peer_id,
                    message=config.FLOOD_MSG,
                    keyboard=keyboard.menu,
                    random_id=0
                )

                await asyncio.sleep(0.1)

            except vk_dev.VkErr as err:
                error_code = int(re.findall(r"\[.+\]", err.text)[0][5:-1])
                if error_code == 7:
                        
                    chats -= 1
                    print(
                        "\033[31m[*]\033[0m Bot kick from chat | "
                        f"Total chats: {chats}"
                    )
                    return

                elif error_code == 9:
                    await asyncio.sleep(5)
                else:
                    print(err)


if __name__ == '__main__':
    lp()



