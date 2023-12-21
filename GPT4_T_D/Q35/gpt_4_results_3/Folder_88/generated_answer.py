
def remove_repeat_chars(my_string):
    my_chars = set()
    for char in my_string[4:9]:
        if my_string.count(char) > 1:
            my_chars.add(char)
    new_string = "".join(char for char in my_string if char not in my_chars)
    return new_string
