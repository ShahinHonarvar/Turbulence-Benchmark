
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[23:75]:
        if 'L' < char <= 'd' and char in vowels:
            result.append(char)
    return result
