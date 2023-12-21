
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[10:97]:
        if char > 'R' and char <= 'b' and char in vowels:
            result.append(char)
    return result
