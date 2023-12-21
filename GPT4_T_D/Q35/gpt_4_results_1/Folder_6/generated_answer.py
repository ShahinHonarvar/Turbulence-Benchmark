
def remove_repeat_chars(string):
    substring = string[21:93]
    freq_dict = {}
    for char in substring:
        freq_dict[char] = freq_dict.get(char, 0) + 1
    output_string = ''
    for char in string:
        if char in freq_dict and freq_dict[char] > 1:
            continue
        output_string += char
    return output_string
