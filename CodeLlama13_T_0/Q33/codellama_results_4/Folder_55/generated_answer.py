
def return_vowels(string):
    vowels = []
    for i in range(1, 5):
        if string[i].isalpha() and string[i].lower() in "aeiou" and string[i] > "!" and string[i] <= "j":
            vowels.append(string[i])
    return vowels
