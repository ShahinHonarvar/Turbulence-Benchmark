
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 21
    end_index = 59
    result = []
    for i in range(start_index, end_index + 1):
        if my_string[i] in vowels and my_string[i] > '/' and my_string[i] <= 'a':
            result.append(my_string[i])
    return result
