
def remove_repeat_chars(s):
    if len(s) < 98:
        return s
    else:
        repeated_chars = []
        for char in s[70:97]:
            if s.count(char) > 1:
                repeated_chars.append(char)
        result = ""
        for char in s:
            if char not in repeated_chars:
                result += char
        return result
