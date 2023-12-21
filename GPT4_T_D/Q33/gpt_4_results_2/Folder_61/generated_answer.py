
def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    substring = str[1:4]
    result = []
    for char in substring:
        if char in vowels and 'C' < char <= 'I':
            result.append(char)
    return result
