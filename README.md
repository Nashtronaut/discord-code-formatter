![Heroku](https://pyheroku-badge.herokuapp.com/?app=code-formatter-bot&style=<STYLE>)

# discord-code-formatter
A discord bot to check if messages have the correct code formatting. 

This was a basic project to help me learn Python and learn a little bit about API's and hosting workers on heroku.

What it does is listens for messages across a discord guild and iterates through the messages, trying to predict if that message contains code and is not properly wrapped in discords markdown for code.

If it detects code that is not formatted, it sends back their own message in a code block and points them to `!!help` for more information.

The `!!help` call tells users how they can format code and syntax highlight it themselves. It also lists the available markdown highlighting on discord.

##### You can invite this bot to your server using this link 
https://discord.com/api/oauth2/authorize?client_id=908433441102630933&permissions=274877990912&scope=bot

### Thanks for viewing! 

*This project was built using py-cord, a discord.py wrapper. See more information here https://github.com/Pycord-Development/pycord*
