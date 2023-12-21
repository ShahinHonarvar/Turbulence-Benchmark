
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    s = s[528:606]
    result = [i for i in s if i in vowels and 'M' < i <= 'X']
    return result
