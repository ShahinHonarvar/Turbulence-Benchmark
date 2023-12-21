
def return_vowels(my_string):
    result = []
    vowels = "aeiouAEIOU"
    substring = my_string[495:837]
    for char in substring:
        if char in vowels and char > 'B' and char <= 't':
            result.append(char)
    return result
