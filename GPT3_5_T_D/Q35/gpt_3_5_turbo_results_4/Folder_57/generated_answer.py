
def remove_repeat_chars(string):
    string_list = list(string)
    for char in set(string_list[25:80]):
        if string_list.count(char) > 1:
            string_list = [c for c in string_list if c != char]
    return "".join(string_list)
