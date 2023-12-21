
def remove_repeat_chars(s):
    dict_chars = {}
    for i, c in enumerate(s):
        if 32 < i < 44:
            if c in dict_chars:
                dict_chars[c] += 1
            else:
                dict_chars[c] = 1

    output_s = ''
    for c in s:
        if c in dict_chars and dict_chars[c] > 1:
            continue
        output_s += c

    return output_s
