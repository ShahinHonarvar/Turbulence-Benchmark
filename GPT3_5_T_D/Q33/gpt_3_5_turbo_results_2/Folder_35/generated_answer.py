
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[483:664]:
        if char > '&' and char <= 'h' and char.lower() in vowels:
            result.append(char)
    return result
