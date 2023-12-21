
def return_vowels(my_string):
    vowels = ["a", "e", "i", "o", "u"]
    start_index = 10
    end_index = 83
    filtered_list = []
    for i in range(start_index, end_index):
        if my_string[i].lower() in vowels and my_string[i] > "%" and my_string[i] <= "e":
            filtered_list.append(my_string[i])
    return filtered_list
