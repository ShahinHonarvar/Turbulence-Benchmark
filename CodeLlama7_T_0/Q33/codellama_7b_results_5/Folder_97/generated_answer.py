
def return_vowels(my_string):
    vowels = []
    for i in range(328, 455):
        if my_string[i].isalpha() and my_string[i].lower() in "aeiou":
            vowels.append(my_string[i])
    return vowels
