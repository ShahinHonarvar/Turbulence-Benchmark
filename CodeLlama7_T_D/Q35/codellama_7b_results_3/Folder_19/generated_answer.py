
def remove_repeat_chars(s):
    for i in range(1, 4):
        if s[i] in s[:i] or s[i] in s[i+1:]:
            continue

        else:

            s = s.replace(s[i], '', 1)

    return s
