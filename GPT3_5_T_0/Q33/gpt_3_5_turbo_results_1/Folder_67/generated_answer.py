
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[21:59]:
        if char in vowels and char > '/' and char <= 'a':
            result.append(char)
    return result
