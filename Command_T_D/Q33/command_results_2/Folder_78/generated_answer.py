def return_vowels(s):
    lst = []
    for i in range(46, 90):
        if s[i] in 'AEIOU':
            lst.append(s[i])
    return lst
