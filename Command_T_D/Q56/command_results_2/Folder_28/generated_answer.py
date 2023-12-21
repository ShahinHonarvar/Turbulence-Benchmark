import re
def all_substring_of_size_n(string):
    if len(string) < 44:
        return []
    if len(string) == 44:
        return [string]
    if string[0] == "":
        return []
    return re.findall(r'(?<=.)[a-z]+', string)
