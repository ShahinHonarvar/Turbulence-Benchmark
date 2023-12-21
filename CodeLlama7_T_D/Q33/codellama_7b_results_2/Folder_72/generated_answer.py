
def return_vowels(my_string):
    vowels = ["a", "e", "i", "o", "u"]
    start_index = 37
    end_index = 57
    filtered_list = []
    for char in my_string[start_index:end_index]:
        if char.isalpha() and char not in filtered_list:
            if char > "*" and char <= "P":
                filtered_list.append(char)
    return filtered_list
