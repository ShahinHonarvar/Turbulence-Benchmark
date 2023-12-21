
def return_vowels(string):
    vowels = []
    for i in range(171, 402):
        if string[i].isalpha() and string[i].lower() in "aeiou":
            if string[i] > "I" and string[i] <= "k":
                vowels.append(string[i])
    return vowels
