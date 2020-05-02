# mcdiscord - Simple Minecraft status bot for Discord

This is a painfully simple Minecraft status bot for Discord. It will show the server's online/ofline status and the current/max player count in the bot user's status text.

To set up a bot account in Discord, follow [these instructions](https://realpython.com/how-to-make-a-discord-bot-python/#how-to-make-a-discord-bot-in-the-developer-portal).

The bot reads its configuration from the environment. This includes the Discord bot token, which isn't necessarily safe. Don't run this on a server if you don't trust the people who have root access to it.

## Installation and Execution
mcdiscord requires Python 3.7 or later.  I'd recommend using something like pipenv, but if you're not familiar then the below instructions should work.

These instructions assume that you have cloned this repository into a directory called "mcdiscord" under your home directory.
```console
user@host:~$ cd mcdiscord
user@host:~/mcdiscord$ sudo pip3 install -r requirements.txt
user@host:~/mcdiscord$ cat >.env
DISCORD_TOKEN=xxxxxxxxxxxxxxxxxx.xxxxxxxxxxxxxxxxxxxxxxxx
MINECRAFT_SERVER=10.0.0.1:25565
DISCORD_STATUS_CHANNEL=99999999999999999999
STATUS_INTERVAL_SECONDS=30
^D
user@host:~/mcdiscord$ python3 mcdiscord.py
```

## Configuration File
The bot reads its configuration from a file in the current directory called `.env`.

### Required Configuration Variables
* DISCORD\_TOKEN - the bot token for the bot account that will be used to connect to Discord
* MINECRAFT\_SERVER - the hostname (or IP address) and port of the Minecraft server to monitor

### Optional Configuration Variables
* STATUS\_INTERVAL\_SECONDS - how often (in seconds) to update the Minecraft server status.  Defaults to 10 seconds
* DISCORD\_STATUS\_CHANNEL - if set, the bot will send update text to the Discord text channel ID provided here 
* MCDISCORD\_DEBUG - if provided and set to anything other than `False` or `0`, will log debugging and status to the console

## Warranty
There's no warranty. In fact, you shouldn't use this for anything and I highly recommend that you don't. If you do decide to use this and bad things happen then it's your problem and your responsibility.

## License
Copyright 2020 Mark Whittington

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
