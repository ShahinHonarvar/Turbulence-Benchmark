
def return_vowels(my_string):
    vowels = ["a", "e", "i", "o", "u"]
    start_index = 34
    end_index = 69
    filtered_vowels = []
    for i in range(start_index, end_index):
        if my_string[i] in vowels and my_string[i] > "_" and my_string[i] <= "o":
            filtered_vowels.append(my_string[i])
    return filtered_vowels
