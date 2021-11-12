import discord


def code_detection(message):
    code_symbols = ['<', '<=', '>', '>=', '=', '==', '||', '&&', '[', ']', '{', '}', '(', ')', ';', ':', '->']
    data_types = ['string', 'int', 'double', 'bool', 'float', 'long', 'char']
    prob = 0
    detection_index = []

    message_split = message.content.split()
    if message_split.contains('```'):
        return 'Message already formatted'
    else:
        for i in range(len(message_split)-1):
            if message_split[i] in data_types:
                prob += 1
                detection_index.append(i)
            for character in message_split[i]:
                if character in code_symbols:
                    prob += 1
                    detection_index.append(i)

    return prob, detection_index[0]


def format_helper():
    syntax_highlighters = {'JavaScript': 'js', 'CSS': 'css', 'C#': 'cs', 'HTML': 'html', 'Python': 'py', 'JSON': 'json',
                           'SQL': 'sql'}

    message_content = 'Here is how you can format for yourself!``````<languagecode>\n//Your code goes ' \
                      'here\n//Remember to not seperate with a space!\n//Available codes are...\n\n'
    for i in syntax_highlighters:
        message_content += f'{i} code = {syntax_highlighters[i]}\n'

    return message_content + '```'
