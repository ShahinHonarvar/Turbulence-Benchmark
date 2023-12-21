 
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[90:97]:
        if char in vowels and char > '_' and char <= 'x':
            result.append(char)
    return result
