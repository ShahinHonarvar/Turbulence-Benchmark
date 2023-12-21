
def return_vowels(string):
    vowels = []
    for i in range(495, 837):
        if string[i].isalpha() and string[i].lower() in "aeiou" and string[i] > "B" and string[i] <= "t":
            vowels.append(string[i])
    return vowels
