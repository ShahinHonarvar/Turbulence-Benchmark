 def return_vowels(my_string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    start_index = 20
    end_index = 43
    filtered_list = []


    for char in my_string[start_index:end_index]:
        if char.isalpha() and char.islower():
            if vowels.__contains__(char):
                filtered_list.append(char)


    return filtered_list
