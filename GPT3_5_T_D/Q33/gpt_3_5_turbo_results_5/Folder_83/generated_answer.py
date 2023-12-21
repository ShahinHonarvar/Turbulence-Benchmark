
def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in string[90:97]:
        if char > '_' and char <= 'x' and char in vowels:
            result.append(char)
    return result
