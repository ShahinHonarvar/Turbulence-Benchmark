
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[90:97]:
        if char > '_' and char <= 'x' and char.lower() in vowels:
            result.append(char)
    return result
