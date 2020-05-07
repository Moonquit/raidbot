import asyncio

import vk_dev

import config
import keyboard
import ggrun
import re


ggrun.preview()

api = vk_dev.Api(
    token=config.TOKEN,
    group_id=config.GROUP_ID,
    v=config.VERSION
)
lp = api >> vk_dev.LongPoll()

global chats
chats = 0

global mess
mess = 0


@lp.message_new()
async def flood(event, pl):
    """
    Flood if it was invited
    """
    
    if (
        'action' in event.object.message and
        event.object.message.action.type == 'chat_invite_user'
    ): 
        global chats 
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
                global mess
                mess += 1
                await asyncio.sleep(0.1)    

            except vk_dev.VkErr as err:
                Error_Code = int(re.findall(r"\[.+\]", err.text)[0][5:-1])
                if Error_Code == 7:
                    chats -= 1
                    print(f'\033[31m[*]\033[0m Bot kick from chat | Total chats: {chats}')
                elif Error_Code == 9: 
                    await asyncio.sleep(5)
                else:
                    print(err) 

            except KeyboardInterrupt:
                    print(f'\033[32m[*]\033[0m Bot stoped! Total chats: {chats} | Total messages: {mess}')    
  


if __name__ == '__main__':
    lp()
