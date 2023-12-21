 def return_vowels(my_string):
    vowels = ["a", "e", "i", "o", "u"]
    start_index = 23
    end_index = 38
    result = []
    for i in range(start_index, end_index):
        if my_string[i].isalpha() and my_string[i] in vowels and ord(my_string[i]) > ord("N") and ord(my_string[i]) <= ord("k"):
            result.append(my_string[i])
    return result
