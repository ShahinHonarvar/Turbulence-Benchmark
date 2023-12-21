
def return_vowels(string):
    vowels = []
    for i in range(483, 664):
        if string[i] > "&" and string[i] <= "h" and string[i].lower() in "aeiou":
            vowels.append(string[i])
    return vowels
