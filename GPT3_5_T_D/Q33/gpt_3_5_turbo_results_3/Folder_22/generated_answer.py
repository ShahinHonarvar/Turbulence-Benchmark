
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[56:90]:
        if char > 'K' and char <= 'z' and char.lower() in vowels:
            result.append(char)
    return result
