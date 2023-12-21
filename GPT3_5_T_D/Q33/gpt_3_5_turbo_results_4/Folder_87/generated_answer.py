
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[34:58]:
        if char > 'b' and char <= 'o' and char in vowels:
            result.append(char)
    return result
