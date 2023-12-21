
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[40:94]:
        if char > 'd' and char <= 'h' and char in vowels:
            result.append(char)
    return result
