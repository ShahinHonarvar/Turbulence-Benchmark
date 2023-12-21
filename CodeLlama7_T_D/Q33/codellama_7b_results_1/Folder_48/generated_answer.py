 def return_vowels(my_string):
    vowels = ["a", "e", "i", "o", "u"]
    start_index = 529
    end_index = 828
    result = []
    for i in range(start_index, end_index + 1):
        if my_string[i] in vowels and my_string[i] > "U" and my_string[i] <= "l":
            result.append(my_string[i])
    return result
