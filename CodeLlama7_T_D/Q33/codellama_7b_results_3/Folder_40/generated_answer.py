
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 2
    end_index = 7
    filtered_vowels = []
    for i in range(start_index, end_index):
        if my_string[i] in vowels and my_string[i] > '^' and my_string[i] <= 'd':
            filtered_vowels.append(my_string[i])
    return filtered_vowels
