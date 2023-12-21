
def return_vowels(string):
    vowels = []
    for i in range(11, 53):
        if string[i].isalpha() and string[i].lower() in ["a", "e", "i", "o", "u"]:
            if (string[i] > "+") and (string[i] <= "W"):
                vowels.append(string[i])
    return vowels
