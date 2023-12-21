import re
def all_substring_of_size_n(string):
    if not string:
        return []
    if len(string) < 88:
        return []
    return [x for x in re.findall(r'(?<=.)[a-z]', string)]
