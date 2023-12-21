
def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = []
    for char in string[65:70]:
        if char in vowels and char > '%' and char <= 'G':
            result.append(char)
    return result
