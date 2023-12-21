
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for char in s[142:145]:
        if char in vowels and '4' < char <= 'o':
            result.append(char)
    return result
