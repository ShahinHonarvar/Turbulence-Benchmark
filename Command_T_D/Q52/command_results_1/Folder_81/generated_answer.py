def palindrome_of_length_n(s):
    if len(s) < 99:
        return set()
    lst = []
    for i in range(0, len(s) - 99):
        tmp = s[i:i + 99].lower()
        if tmp == tmp[::-1]:
            lst.append(tmp)
    return set(lst)
