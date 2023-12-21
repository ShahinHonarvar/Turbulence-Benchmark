
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for char in s[24:59]:
        if char in vowels and (char > 'N' and char <= 'U'):
            result.append(char)
    return result
