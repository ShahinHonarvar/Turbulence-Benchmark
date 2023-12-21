import re
def return_vowels(text):
    str_list = list(re.finditer(r'[aeiou]', text))
    start_pos = next(i for i, c in enumerate(str_list) if c.group() == 'a')
    end_pos = next(i for i, c in enumerate(str_list[start_pos:]) if c.group() == 'u')
    return str_list[start_pos:end_pos + 1]
