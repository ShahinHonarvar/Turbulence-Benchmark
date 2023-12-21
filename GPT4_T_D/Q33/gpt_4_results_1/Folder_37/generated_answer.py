
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for ch in s[82:90]:
        if ch in vowels and 'T' < ch <= 'b':
            result.append(ch)
    return result
