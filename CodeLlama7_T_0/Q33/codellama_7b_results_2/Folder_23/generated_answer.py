
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 56
    end_index = 96
    result = []
    for i in range(start_index, end_index + 1):
        if my_string[i].isalpha() and my_string[i].lower() in vowels and my_string[i] > '&' and my_string[i] <= 'T':
            result.append(my_string[i])
    return result
