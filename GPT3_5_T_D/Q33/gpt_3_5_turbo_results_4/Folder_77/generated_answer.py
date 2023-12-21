
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[837:975]:
        if char.isalpha() and char.lower() in vowels and char > 'N' and char <= 'W':
            result.append(char)
    return result
