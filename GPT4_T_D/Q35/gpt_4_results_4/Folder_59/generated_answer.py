
def remove_repeat_chars(s):
    temp = list(s)
    for i in range(1, min(10, len(temp))):
        if s.count(temp[i]) > 1:
            temp = [char for char in temp if char != temp[i]]
    return "".join(temp)
