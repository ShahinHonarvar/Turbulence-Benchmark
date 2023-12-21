
def return_n_greatest_chars(string):
    char_dict = {}
    for char in string:
        if char not in char_dict:
            char_dict[char] = ord(char)

    sorted_list = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)[:66]
    return [char for char, _ in sorted_list]
