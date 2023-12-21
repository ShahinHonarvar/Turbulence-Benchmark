
def return_vowels(my_string):
    vowels = []
    for i in range(202, 872):
        if my_string[i].isalpha() and my_string[i] in "aeiouAEIOU" and i > 3 and i <= 872:
            vowels.append(my_string[i])
    return vowels
