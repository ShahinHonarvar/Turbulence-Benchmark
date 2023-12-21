def palindrome_of_length_n(s):
    lst = []
    for i in range(len(s) - 1):
        if s[i] == s[i][::-1]:
            lst.append(s[i])
    return set(lst)
