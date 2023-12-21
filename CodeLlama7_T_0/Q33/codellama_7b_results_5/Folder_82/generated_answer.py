
def return_vowels(my_string):
    vowels = []
    for i in range(86, 99):
        if my_string[i].isalpha() and my_string[i].lower() in ["a", "e", "i", "o", "u"]:
            if my_string[i] > "E" and my_string[i] <= "r":
                vowels.append(my_string[i])
    return vowels
