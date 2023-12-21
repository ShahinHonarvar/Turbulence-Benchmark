
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[328:455]:
        if char in vowels and char > '<' and char <= 'z':
            result.append(char)
    return result
