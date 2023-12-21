
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[21:23]:
        if char in vowels and char > '-' and char <= 'n':
            result.append(char)
    return result
