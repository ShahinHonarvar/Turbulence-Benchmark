 def return_vowels(my_string):
    vowels = ["a", "e", "i", "o", "u"]
    start_index = 23
    end_index = 75
    result = []
    for i in range(start_index, end_index + 1):
        if my_string[i] in vowels and my_string[i].islower():
            if "L" <= my_string[i] <= "d":
                result.append(my_string[i])
    return result
