def return_vowels(s):
    lst = []
    for i in range(77, 84):
        if i > ord(s[0]) and i <= ord('G'):
            lst.append(chr(i))
    return lst
