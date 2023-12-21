
def return_vowels(my_string):
    vowels = ["A", "E", "I", "O", "U"]
    start_index = 14
    end_index = 60
    filtered_vowels = []
    for i in range(start_index, end_index):
        if my_string[i] in vowels and my_string[i] > "D" and my_string[i] <= "V":
            filtered_vowels.append(my_string[i])
    return filtered_vowels
