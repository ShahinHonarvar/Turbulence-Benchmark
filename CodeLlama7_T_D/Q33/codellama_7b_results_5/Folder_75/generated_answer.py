
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(20, 41):
        if my_string[i].isalpha() and my_string[i].lower() in vowels and my_string[i] > 'K' and my_string[i] <= 'Z':
            result.append(my_string[i])
    return result
