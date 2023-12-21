
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[10:83]:
        if char in vowels and char > '%' and char <= 'e':
            result.append(char)
    return result
