
def return_vowels(my_string):
    vowels = ["a", "e", "i", "o", "u"]
    start_index = 10
    end_index = 82
    filtered_list = []
    for char in my_string[start_index:end_index]:
        if char in vowels and char > "$" and char <= "@":
            filtered_list.append(char)
    return filtered_list
