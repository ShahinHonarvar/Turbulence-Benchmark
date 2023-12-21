
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 170
    end_index = 645
    filtered_list = []
    for i in range(start_index, end_index + 1):
        if my_string[i].isalpha():
            if my_string[i] > 'E' and my_string[i] <= '~':
                filtered_list.append(my_string[i])
    return filtered_list
