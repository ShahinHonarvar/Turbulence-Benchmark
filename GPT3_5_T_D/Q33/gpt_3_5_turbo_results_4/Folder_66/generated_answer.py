
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[63:79]:
        if char > 'D' and char <= 'y' and char.lower() in vowels:
            result.append(char)
    return result
