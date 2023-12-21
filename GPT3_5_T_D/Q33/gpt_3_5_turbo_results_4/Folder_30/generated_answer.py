
def return_vowels(string):
    vowels = []
    for i in range(11, 61):
        if string[i] > "M" and string[i] <= "W" and string[i].lower() in "aeiou":
            vowels.append(string[i])
    return vowels
