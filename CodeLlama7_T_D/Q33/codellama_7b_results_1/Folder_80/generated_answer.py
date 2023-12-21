
def return_vowels(my_string):
    vowels = []
    for i in range(85, 99):
        if my_string[i] in "aeiou" and my_string[i] > "/" and my_string[i] <= "n":
            vowels.append(my_string[i])
    return vowels
