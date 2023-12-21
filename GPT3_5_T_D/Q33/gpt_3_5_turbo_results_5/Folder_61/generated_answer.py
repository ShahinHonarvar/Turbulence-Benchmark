
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[1:4]:
        if 'C' < char <= 'I' and char.lower() in vowels:
            result.append(char)
    return result
