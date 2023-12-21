
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[21:23]:
        if char >= '-' and char <= 'n' and char in vowels:
            result.append(char)
    return result
