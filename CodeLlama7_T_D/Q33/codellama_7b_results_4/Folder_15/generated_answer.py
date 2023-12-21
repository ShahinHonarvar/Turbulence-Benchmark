
def return_vowels(my_string):
    vowels = ["a", "e", "i", "o", "u"]
    start_index = 5
    end_index = 6
    result = []
    for i in range(start_index, end_index):
        if my_string[i].lower() in vowels and my_string[i] > my_string[3] and my_string[i] <= "^":
            result.append(my_string[i])
    return result
