
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 20
    end_index = 34
    result = []
    for i in range(start_index, end_index):
        if my_string[i] in vowels and my_string[i] > 'U' and my_string[i] <= 'i':
            result.append(my_string[i])
    return result
