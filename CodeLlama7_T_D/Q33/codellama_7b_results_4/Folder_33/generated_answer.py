 def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 163
    end_index = 771
    filtered_list = []
    for i in range(start_index, end_index + 1):
        if my_string[i] in vowels and my_string[i] > ':' and my_string[i] <= 'E':
            filtered_list.append(my_string[i])
    return filtered_list
