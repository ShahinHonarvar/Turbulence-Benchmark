 def filter_chars(s):
    result = ""
    for i in range(318, 337):
        if s[i] > 'B' and s[i] < 'z':
            continue

        else:

            result += s[i]

    return result
