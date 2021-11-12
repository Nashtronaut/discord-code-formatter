
# Code detection works on a simple probability calculator. It is trying to detect uncommon symbols and patterns
# used in code. If servers find the bot to be too sensitive, increase required probability in bot.py trigger

def code_detection(message):
    code_symbols = ['<', '<=', '>', '>=', '=', '==', '||', '&&', '[', ']', '{', '}', '(', ')', ';', ':', '->', '#']
    data_types = ['string', 'int', 'double', 'bool', 'float', 'long', 'char', 'bash', 'bin']
    prob: int = 0

    message_split = message.content.split()
    for message_section in message_split:
        if message_section.startswith('```'): # ignores messages that code blocks are detected in
            return
        if message_section in data_types:
            prob += 1
        else:
            for character in message_section:
                if character in code_symbols:
                    prob += 1
    return prob
    
def format_helper():
    syntax_highlighters = {'Ascii Doc': 'asciidoc', 'Auto Hot Key': 'autohotkey', 'Bash': 'bash',
                           'Coffee Script': 'coffeescript', 'C++': 'cpp', 'C#': 'cs', 'CSS': 'css',
                           'Git Diff (+ -)': 'diff', 'Fix': 'fix', 'GLSL': 'glsl', 'ini': 'ini',
                           'JSON': 'json', 'Markdown': 'md', 'Machine Learning': 'ml',
                           'Pro Log': 'prolog', 'Python': 'py', 'XL': 'xl', 'XML': 'xml'}

    message_content = 'Here is how you can format for yourself!``````<language_code>\n//<Your code goes here>\n//End code block with three more backticks\n//Don\'t separate language code and backticks with a space!\n//Available codes are...\n\n'
    for i in syntax_highlighters:
        message_content += f'{i} = {syntax_highlighters[i]}\n'

    return message_content + '```\nCheck this out for more markdown ' \
                             'tips!\n<https://support.discord.com/hc/en-us/articles/210298617-Markdown-Text' \
                             '-101-Chat-Formatting-Bold-Italic-Underline-> '
