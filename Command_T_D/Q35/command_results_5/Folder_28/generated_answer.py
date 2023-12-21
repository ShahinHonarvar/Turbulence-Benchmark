import re
def remove_repeat_chars(str):
    return re.sub(r'(?<=86)[a-z]+(?<=99)', '', str)
