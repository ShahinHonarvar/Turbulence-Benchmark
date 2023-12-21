
def return_vowels(my_string):
    vowels = ["a", "e", "i", "o", "u"]
    result = []
    for i in range(2, 7):
        if my_string[i] in vowels and my_string[i] > "^" and my_string[i] <= "d":
            result.append(my_string[i])
    return result
