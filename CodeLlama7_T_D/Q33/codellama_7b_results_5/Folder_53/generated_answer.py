
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 27
    end_index = 57
    result = []
    for i in range(start_index, end_index):
        if my_string[i].isalpha() and my_string[i].lower() in vowels and my_string[i] > 'o' and my_string[i] <= 'w':
            result.append(my_string[i])
    return result
