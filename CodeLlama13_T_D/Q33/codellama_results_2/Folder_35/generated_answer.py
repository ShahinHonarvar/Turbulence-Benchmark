
def return_vowels(string):
    vowels = []
    for i in range(483, 664):
        if string[i].lower() in "aeiou" and string[i] <= "h":
            vowels.append(string[i])
    return vowels
