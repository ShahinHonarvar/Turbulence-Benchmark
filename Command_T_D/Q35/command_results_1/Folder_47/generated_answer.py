def remove_repeat_chars(s):
    result = s[:29] + s[30:-53] + s[54:]
    for c in s[29:-53]:
        result = result.replace(c, "")
    return result
