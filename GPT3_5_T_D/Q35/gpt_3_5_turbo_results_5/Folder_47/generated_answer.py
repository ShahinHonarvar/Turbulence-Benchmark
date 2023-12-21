
def remove_repeat_chars(string):
    indices = range(30, 53)
    unique_chars = []
    for index, char in enumerate(string):
        if index in indices and char in unique_chars:
            string = string.replace(char, "")
        elif index in indices and char not in unique_chars:
            unique_chars.append(char)
  
    return string
