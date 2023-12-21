
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[1:4]:
        if char > 'C' and char <= 'I' and char in vowels:
            result.append(char)
    return result
