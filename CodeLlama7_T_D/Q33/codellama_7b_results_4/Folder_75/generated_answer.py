
def return_vowels(my_string):
    vowels = ["a", "e", "i", "o", "u"]
    start_index = 20
    end_index = 41
    result = []
    for i in range(start_index, end_index + 1):
        if my_string[i].isalpha():
            if my_string[i] > "K" and my_string[i] <= "Z":
                result.append(my_string[i])
    return result
