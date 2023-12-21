
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(55, 65):
        if my_string[i].isalpha() and my_string[i] > 'Z' and my_string[i] <= 'w':
            result.append(my_string[i])
    return result
