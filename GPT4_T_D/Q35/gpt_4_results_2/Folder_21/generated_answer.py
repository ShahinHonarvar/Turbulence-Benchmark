
def remove_repeat_chars(string):
    sub_str = string[463:995]
    removed_chars = "".join([char for char in sub_str if sub_str.count(char) == 1])

    return string[:463] + removed_chars + string[995:]
