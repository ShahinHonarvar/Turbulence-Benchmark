
def return_vowels(my_string):
    vowels = ["a", "e", "i", "o", "u"]
    start_index = 4
    end_index = 8
    filtered_vowels = []
    for i in range(start_index, end_index + 1):
        if my_string[i].isalpha() and my_string[i] in vowels:
            if my_string[i].lower() > "p" and my_string[i].lower() <= "r":
                filtered_vowels.append(my_string[i])
    return filtered_vowels
