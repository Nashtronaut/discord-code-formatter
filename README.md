[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

![Heroku](http://heroku-badge.herokuapp.com/?app=heroku-badge&root=bot.py)



# discord-code-formatter
A discord bot to check if messages have the correct code formatting. 

This was a basic project to help me learn some Python, learn a little bit about API's and hosting workers on heroku.

What it does is listens for messages with code inside, that are not formatted properly. 

For example, if someone copy and pastes code into a guild for help without using code blocks or syntax highlighting.

If the bot detects code in the message, it will return the message back in the same channel properly highlighted and formatted based on guesslang's best guess.
guesslang is not a perfect library in terms of guessing languages, but it works for this purpose. Besides, we don't want the bot triggering for smaller messages anyway.

Unfortunately, I had to disable .INI code detection as some regular messages were flagging the bot. 

The `!!help` call tells users how they can format code and syntax highlight it themselves. It also links to some documenatation about it.

##### You can invite this bot to your server using this link 
https://discord.com/api/oauth2/authorize?client_id=908433441102630933&permissions=274877990912&scope=bot

![image](https://user-images.githubusercontent.com/48274410/143137680-2f00a9f5-bd96-44a4-ac8b-7ecf58db11ed.png)

### Thanks for viewing! 

*This project was built using py-cord, a discord.py wrapper. See more information here https://github.com/Pycord-Development/pycord*

*This project also uses a library called guesslang, a library to identify code languages from strings. See more here https://github.com/yoeo/guesslang*
