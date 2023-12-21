def remove_repeat_chars(str):
    lst = str[36:54]
    for i in range(len(lst)):
        cnt = lst.count(lst[i])
        if cnt > 1:
            lst = lst.replace(lst[i], '')
    return str[0:36] + lst + str[54:]
