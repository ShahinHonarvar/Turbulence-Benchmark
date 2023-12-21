 def return_vowels(my_string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    start_index = 495
    end_index = 837
    filtered_list = []
    for i in range(start_index, end_index + 1):
        if my_string[i].isalpha() and my_string[i] not in vowels:
            filtered_list.append(my_string[i])
    return filtered_list
