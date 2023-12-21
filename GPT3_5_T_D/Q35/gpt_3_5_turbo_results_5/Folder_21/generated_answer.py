
def remove_repeat_chars(string):
    start = 462
    end = 995
    altered_string = ""
    for i in range(len(string)):
        if i >= start and i < end:
            if string[i] != string[start:end].count(string[i]):
                altered_string += string[i]
        else:
            altered_string += string[i]
    return altered_string
