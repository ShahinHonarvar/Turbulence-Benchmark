
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[641:872]:
        if char in vowels and char > '>' and char <= 'q':
            result.append(char)
    return result
