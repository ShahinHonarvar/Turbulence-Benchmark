
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for ch in s[770:852]:
        if ch in vowels and 'B' < ch <= 'i':
            result.append(ch)
    return result
