
def remove_repeat_chars(string):
    seen = {}
    result = ""
    for i, c in enumerate(string[13:91]):
        if c not in seen or seen[c] == 0:
            seen[c] = 1
            result += c
        else:
            seen[c] -= 1
    return result + string[91:]
