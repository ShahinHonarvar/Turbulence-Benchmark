
def return_vowels(my_string):
    vowels = ["a", "e", "i", "o", "u"]
    start_index = 43
    end_index = 70
    filtered_list = []
    for char in my_string[start_index:end_index]:
        if char.isalpha() and char not in filtered_list and char > "*":
            filtered_list.append(char)

    return filtered_list
