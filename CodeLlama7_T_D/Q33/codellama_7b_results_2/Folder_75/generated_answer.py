
def return_vowels(my_string):
    vowels = []
    for i in range(20, 41):
        if my_string[i].isalpha() and my_string[i].lower() in "aeiou" and my_string[i] > "K" and my_string[i] <= "Z":
            vowels.append(my_string[i])
    return vowels
