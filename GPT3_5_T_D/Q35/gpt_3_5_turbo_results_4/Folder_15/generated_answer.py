
def remove_repeat_chars(string):
    count = {}
    for i in range(len(string)):
        if i < 4 and string[i] not in count:
            count[string[i]] = 1
        elif i < 4:
            count[string[i]] += 1
        elif count.get(string[i]) is not None and count[string[i]] > 1:
            string = string.replace(string[i], '')
    return string
