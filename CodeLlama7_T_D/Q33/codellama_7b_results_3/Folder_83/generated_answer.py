
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(90, 97):
        if my_string[i] in vowels and my_string[i] > '_' and my_string[i] <= 'x':
            result.append(my_string[i])
    return result
