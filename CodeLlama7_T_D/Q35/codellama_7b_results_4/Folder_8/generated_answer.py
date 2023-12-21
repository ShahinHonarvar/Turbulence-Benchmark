 def remove_repeat_chars(s):
    result = ""
    for i in range(len(s)):
        if s[i] not in s[45:48]:
            result += s[i]
    return result
