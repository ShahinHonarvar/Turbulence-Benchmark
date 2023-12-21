
def return_n_greatest_chars(string):
    char_dict = {}
    for char in string:
        if char not in char_dict:
            char_dict[char] = ord(char)
    sorted_list = sorted(char_dict, key=lambda x: char_dict[x], reverse=True)[:37]
    return "".join(sorted_list)
