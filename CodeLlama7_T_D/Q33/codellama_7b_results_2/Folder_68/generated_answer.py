
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 1
    end_index = 9
    filtered_list = []

    for i in range(start_index, end_index):
        if my_string[i].lower() in vowels:
            if my_string[i] > '?':
                if my_string[i] <= 'k':
                    filtered_list.append(my_string[i])

    return filtered_list
