from guesslang import Guess

syntax_highlighters = {'Ascii Doc': 'asciidoc', 'Auto Hot Key': 'autohotkey', 'Bash': 'bash',
                       'Coffeescript': 'coffeescript', 'C++': 'cpp', 'C#': 'cs', 'CSS': 'css',
                       'Git Diff (+ -)': 'diff', 'Fix': 'fix', 'GLSL': 'glsl', 'INI': 'ini',
                       'JSON': 'json', 'Markdown': 'md', 'Machine Learning': 'ml',
                       'Prolog': 'prolog', 'Python': 'py', 'XL': 'xl', 'XML': 'xml'}


def code_detection(message):
    guess = Guess()
    highlighter_code = ''
    lang_guess = guess.language_name(message)

    if lang_guess in syntax_highlighters:
        highlighter_code = syntax_highlighters[lang_guess]

    print(highlighter_code)
    return highlighter_code


def format_helper():
    message_content = 'Here is how you can format for yourself!``````<language_code>\n//<Your code goes here>\n//End ' \
                      'code block with three more backticks\n//Don\'t separate language code and backticks with a ' \
                      'space!\n//Available codes are...\n\n '
    for i in syntax_highlighters:
        message_content += f'{i} = {syntax_highlighters[i]}\n'

    return message_content + '```\nCheck this out for more markdown ' \
                             'tips!\n<https://support.discord.com/hc/en-us/articles/210298617-Markdown-Text' \
                             '-101-Chat-Formatting-Bold-Italic-Underline-> '
