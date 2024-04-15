
# Discord-Clear-Bot V1 📌

> `NOTE 📝:` This is a fully customizable discord.py bot with a clear command.

# Table of Contents
- [Features](#features)
- [Bot Usage](#bot-usage)
- [Commands](#commands)
  - [Clear Command](#clear-command)
- [Installation](#installation)
- [Configuration](#configuration)
- [Pictures](#pictures)


## Features

- **Clear Command** Clear a specific amount of messages in a channel.
- **Clear logs** The bot automatically sends a log message in the channel you defined. 

## Bot Usage
To use this bot, follow these steps: 
+ set up a bot on https://discord.com/developers/applications
+ get your bot token and put the token in the token.txt
+ Invite the bot to your Discord server 
+ Run the bot by putting your token in the `"token.txt"`, no other characters



## Commands

### Clear Command

- **Description:** Delete messages in a channel.
- **Usage:** `.clear`, `[aliases]` 
  - `aliases`: You can use `".delete"`, `".purge"` too.
- **Permissions Required:** manage messages

> [!IMPORTANT]
> The warning message for invalid numbers only shows up if you put no number after the .clear; .delete; .purge; else an error appears im about to fix this error soon.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/TrapstarJannik/Discord-Clear-Bot.git
    ```
   ```sh
   cd Discord-Clear-Bot
   ```

4. Run the bot:
   ```sh
   python main.py
   ```
   
> [!IMPORTANT]
> You need to put your token in the `token.txt` or you will get an error!

## Configuration

- The bot's prefix is set to `.` by default. You can change it in the `main.py` file.
- add your discord bot token in the `token.txt` by replacing the first line.

## Pictures

![Screenshot_60](https://github.com/TrapstarJannik/Discord-Slash-Command/assets/166982775/71d5cd6b-6b17-4a0e-9129-d03b9a15bc82)




