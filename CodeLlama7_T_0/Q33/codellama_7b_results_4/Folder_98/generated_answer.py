
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 3
    end_index = 9
    result = []
    for i in range(start_index, end_index):
        if my_string[i].lower() in vowels and my_string[i] > 'S' and my_string[i] <= 'U':
            result.append(my_string[i])
    return result
