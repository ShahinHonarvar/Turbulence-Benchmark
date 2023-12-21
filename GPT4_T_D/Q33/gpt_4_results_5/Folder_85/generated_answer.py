
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    sub_string = s[55:65]
    result = []
    for char in sub_string:
        if char in vowels and 'Z' < char <= 'w':
            result.append(char)
    return result
