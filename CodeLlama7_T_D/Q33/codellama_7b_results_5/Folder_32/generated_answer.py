
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 45
    end_index = 76
    result = []

    for i in range(start_index, end_index):
        if my_string[i].lower() in vowels and my_string[i] > 'b' and my_string[i] <= 'z':
            result.append(my_string[i])

    return result
