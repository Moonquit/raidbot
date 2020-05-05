import asyncio

import vk_dev

import config
import keyboard
import ggrun

chats = 0

ggrun.preview()

api = vk_dev.Api(
    token=config.TOKEN,
    group_id=config.GROUP_ID,
    v=config.VERSION
)
lp = api >> vk_dev.LongPoll()


@lp.message_new()
async def flood(event, pl):
    """
    Flood if it was invited
    """
    if (
        'action' in event.object.message and
        event.object.message.action.type == 'chat_invite_user'
    ): 
        chats += 1
        print(f'\033[31m[*]\033[0m New chat | Total chats: {chats}')
        while True:
            try:
                await api.messages.send(
                    peer_id=event.object.message.peer_id,
                    message=config.FLOOD_MSG,
                    keyboard=keyboard.menu,
                    random_id=0
                )
                await asyncio.sleep(0.1)
            except Exception:
                await asyncio.sleep(5)


if __name__ == '__main__':
    lp()
