
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[65:70]:
        if char in vowels and char > '%' and char <= 'G':
            result.append(char)
    return result
