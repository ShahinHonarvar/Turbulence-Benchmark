
def return_vowels(my_string):
    vowels = ["a", "e", "i", "o", "u"]
    start_index = 44
    end_index = 95
    filtered_list = []
    for char in my_string[start_index:end_index]:
        if char.isalpha() and char.lower() in vowels and char > "5" and char <= "<":
            filtered_list.append(char)
    return filtered_list
