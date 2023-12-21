
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[202:872]:
        if char > '3' and char <= '>':
            if char.lower() in vowels:
                result.append(char)
    return result
