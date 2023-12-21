
def remove_repeat_chars(s):
    temp_dict = {}
    for i in range(91, 97):
        if s[i] in temp_dict:
            temp_dict[s[i]] += 1
        else:
            temp_dict[s[i]] = 1
    repeated_chars = [key for (key, value) in temp_dict.items() if value > 1]
    return ''.join([char for char in s if char not in repeated_chars])
