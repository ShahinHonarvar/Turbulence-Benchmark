
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 23
    end_index = 85
    result = []
    for i in range(start_index, end_index + 1):
        if my_string[i].isalpha() and my_string[i] > 'W' and my_string[i] <= 'v':
            result.append(my_string[i])
    return result
