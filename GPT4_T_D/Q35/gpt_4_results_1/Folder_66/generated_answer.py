
def remove_repeat_chars(s):
    if len(s) <= 77:
        return s
    else:
        char_set = set()
        result = ''
        for i in range(len(s)):
            if 10 < i < 76:
                if s[i] not in char_set:
                    char_set.add(s[i])
                else:
                    continue
            result += s[i]
    
    return result
