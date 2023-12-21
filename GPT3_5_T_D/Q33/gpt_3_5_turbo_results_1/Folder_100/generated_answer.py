
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[23:75]:
        if char in vowels and 'L' < char <= 'd':
            result.append(char)
    return result
