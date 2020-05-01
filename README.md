# Raidbot
> Raid bot for vk.com
## Run
At the main repo directory run `code` like a module:
```bash
cd raidbot
python3 -m code
```
## Config params
Make `config.py` at the `raidbot/code/` directory and add this params

|Name|Type|Description|
|:-:|:-:|:-|
|TOKEN|str|Your API token|
|VERSION|str|API version. Recommend '5.123'|
|GROUP_ID|int|VK group id|
|FLOOD_MSG|str|Flooad message|

## Abilities
_Will be added later_

## Recommendations
Create virtual enviroment and install packages there
```bash
cd raidbot
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```
After session you can deacticate your env
```bash
deactivate
```
