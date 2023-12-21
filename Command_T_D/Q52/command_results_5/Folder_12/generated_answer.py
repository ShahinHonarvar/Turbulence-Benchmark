def palindrome_of_length_n(s):
    lst = []
    for i in range(len(s) - 1):
        if s[i] == s[len(s) - 1 - i]:
            lst.append(s[i])
        else:
            break
    return set(lst)
