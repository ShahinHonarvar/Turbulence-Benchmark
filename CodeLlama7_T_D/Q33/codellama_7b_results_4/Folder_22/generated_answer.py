 def return_vowels(my_string):
    vowels = ["a", "e", "i", "o", "u"]
    start_index = 56
    end_index = 90
    filtered_list = []
    for char in my_string[start_index:end_index]:
        if char.isalpha() and char.islower():
            if vowels.__contains__(char):
                filtered_list.append(char)
    return filtered_list
