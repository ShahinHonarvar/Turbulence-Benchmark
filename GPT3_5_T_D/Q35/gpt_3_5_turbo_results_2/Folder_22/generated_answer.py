
def remove_repeat_chars(string):
    start_index = 50
    end_index = 200
    repeated_chars = [char for char in string[start_index:end_index] if string[start_index:end_index].count(char) > 1]
    for char in repeated_chars:
        string = string.replace(char, "")
    return string
