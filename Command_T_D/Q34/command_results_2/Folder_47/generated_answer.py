def find_original_set(s):
    lst = []
    for i in range(len(s)):
        lst.append(set(s[i]))
    return min(lst)
