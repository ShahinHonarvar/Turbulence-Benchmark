
def filter_chars(string):
    if len(string) < 16:
        return string
    else:
        start = 10
        end = 15

        sub_string = string[start:end]
        new_string = ""
        for i in range(len(sub_string)):
            if sub_string[i] > 't' and sub_string[i] < 'v':
                continue
            else:
                new_string += sub_string[i]

        return string[:start] + new_string + string[end:]
