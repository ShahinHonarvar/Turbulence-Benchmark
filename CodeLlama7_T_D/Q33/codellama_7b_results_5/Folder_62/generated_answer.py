
def return_vowels(my_string):
    vowels = ["a", "e", "i", "o", "u"]
    start_index = 14
    end_index = 60
    filtered_list = []
    for i in range(start_index, end_index + 1):
        current_char = my_string[i]
        if current_char > "D" and current_char <= "v":
            filtered_list.append(current_char)
    return filtered_list
