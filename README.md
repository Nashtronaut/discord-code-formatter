[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

![Heroku](http://heroku-badge.herokuapp.com/?app=heroku-badge&root=bot.py)



# discord-code-formatter
A discord bot to check if messages have the correct code formatting. 

This was a basic project to help me learn Python and learn a little bit about API's and hosting workers on heroku.

What it does is listens for messages with code inside, that are not formatted properly. 

For example, if someone copy and pastes code into a guild for help with using code blocks or syntax highlighting.

If the bot detects code in the message, it will return the message back in the same channel properly highlighted and formatted based on guesslang's best guess.
guesslang is not a perfect library in terms of guessing languages, but it works for this purpose. Besides, we don't want the bot triggering for smaller messages anyway.

Unfortunately, I had to disable .INI code detection as some regular messages were flagging the bot. 

The `!!help` call tells users how they can format code and syntax highlight it themselves. It also lists the available markdown highlighting on discord.

##### You can invite this bot to your server using this link 
https://discord.com/api/oauth2/authorize?client_id=908433441102630933&permissions=274877990912&scope=bot

![Screenshot 2021-11-12 214707](https://user-images.githubusercontent.com/48274410/141606006-64dd3ff4-33d0-4f30-94a2-3c9741921b78.png)

### Thanks for viewing! 

*This project was built using py-cord, a discord.py wrapper. See more information here https://github.com/Pycord-Development/pycord*

*This project also uses a library called guesslang, a library to identify code languages from strings. See more here https://github.com/yoeo/guesslang*
