import discord


def code_detection(message):
    code_symbols = ['<', '<=', '>', '>=', '=', '==', '||', '&&', '[', ']', '{', '}', '(', ')', ';', ':', '->']
    data_types = ['string', 'int', 'double', 'bool', 'float', 'long', 'char']
    prob = 0

    message_split = message.content.split()
    if '```' in message_split:
        return 'Message already formatted'
    else:
        for i in range(len(message_split) - 1):
            if message_split[i] in data_types:
                prob += 1
            for character in message_split[i]:
                if character in code_symbols:
                    prob += 1

    return prob


def format_helper():
    syntax_highlighters = {'JavaScript': 'js', 'CSS': 'css', 'C#': 'cs', 'HTML': 'html', 'Python': 'py', 'JSON': 'json',
                           'SQL': 'sql'}

    message_content = 'Here is how you can format for yourself!``````<language_code>\n//Your code goes ' \
                      'here\n//Remember to not separate with a space!\n//Available codes are...\n\n'
    for i in syntax_highlighters:
        message_content += f'{i} code = {syntax_highlighters[i]}\n'

    return message_content + '```'
