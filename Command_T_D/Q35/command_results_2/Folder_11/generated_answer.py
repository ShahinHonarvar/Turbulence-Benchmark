import re
def remove_repeat_chars(s):
    return re.sub(r'((?<=<)A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z)(?=>)', '', s)
