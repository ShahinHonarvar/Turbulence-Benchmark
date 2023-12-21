 def return_vowels(my_string):
    vowels = ["a", "e", "i", "o", "u"]
    start_index = 13
    end_index = 35
    result = []
    for i in range(start_index, end_index):
        if my_string[i].isalpha() and my_string[i] in vowels and my_string[i] > "8" and my_string[i] <= "F":
            result.append(my_string[i])
    return result
