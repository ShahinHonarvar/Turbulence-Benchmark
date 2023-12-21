
def return_vowels(my_string):
    vowels = []
    for i in range(483, 665):
        if my_string[i].isalpha() and my_string[i].lower() in ["a", "e", "i", "o", "u"]:
            if my_string[i] > "&" and my_string[i] <= "h":
                vowels.append(my_string[i])
    return vowels
