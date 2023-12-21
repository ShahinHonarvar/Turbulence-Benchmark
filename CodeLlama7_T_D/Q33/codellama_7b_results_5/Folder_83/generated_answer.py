
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in my_string[90:97]:
        if char in vowels and char > '_' and char <= 'x':
            result.append(char)
    return result
