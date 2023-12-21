
def remove_repeat_chars(string):
    start_index = 13
    end_index = 76
    unique_chars = set()
    duplicate_chars = set()

    for i in range(start_index, end_index):
        char = string[i]
        if char in unique_chars:
            duplicate_chars.add(char)
        unique_chars.add(char)
    
    for char in duplicate_chars:
        string = string.replace(char, "")

    return string
