
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 40
    end_index = 91
    result = []
    for i in range(start_index, end_index):
        if my_string[i].lower() in vowels and my_string[i] > 'a' and my_string[i] <= 'x':
            result.append(my_string[i])
    return result
