 def return_vowels(my_string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    start_index = 528
    end_index = 606
    filtered_list = []
    for i in range(start_index, end_index):
        if my_string[i].isalpha() and my_string[i] > 'M' and my_string[i] <= 'X':
            filtered_list.append(my_string[i])
    return filtered_list
