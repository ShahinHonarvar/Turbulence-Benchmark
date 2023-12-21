def palindrome_of_length_n(s):
    lst = []
    for i in range(len(s)):
        c = s[i]
        if c.lower() in 'qwertyuiopasdfghjklzxcvbnm':
            lst.append(s[i])
            lst.append(s[i:])
            break
    return set(lst)
