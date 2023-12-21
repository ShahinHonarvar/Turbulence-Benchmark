
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 70
    end_index = 76
    filtered_list = []











    for i in range(start_index, end_index):
        if my_string[i] in vowels and my_string[i] > '2' and my_string[i] <= ':':
            filtered_list.append(my_string[i])

    return filtered_list
