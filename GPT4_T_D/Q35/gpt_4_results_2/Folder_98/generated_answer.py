
def remove_repeat_chars(s):
    temp_set = set()
    repeat_chars = []
    for i in range(1, 8):
        if i < len(s) and s[i] in temp_set:
            repeat_chars.append(s[i])
        else:
            temp_set.add(s[i])
    new_s = "".join([char for char in s if char not in repeat_chars])
    return new_s
