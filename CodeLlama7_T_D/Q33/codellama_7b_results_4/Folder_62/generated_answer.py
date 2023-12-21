
def return_vowels(my_string):
    vowels = ["a", "e", "i", "o", "u"]
    start_index = 14
    end_index = 60
    result = []
    for i in range(start_index, end_index):
        if my_string[i].lower() in vowels and my_string[i] > "d" and my_string[i] <= "v":
            result.append(my_string[i])
    return result
