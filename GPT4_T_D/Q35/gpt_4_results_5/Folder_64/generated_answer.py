
def remove_repeat_chars(s):
    count_dict = {}
    for i in range(1, 5):
        if s[i] in count_dict:
            count_dict[s[i]] += 1
        else:
            count_dict[s[i]] = 1
            
    return ''.join([char for char in s if count_dict.get(char, 0) == 1])
