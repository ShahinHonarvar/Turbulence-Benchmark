
def return_vowels(s):
    vowels = 'aeiou'
    s_sub = s[47:89]
    result = []
    for char in s_sub:
        if char > '@' and char <= 'n' and char in vowels:
            result.append(char)
    return result
