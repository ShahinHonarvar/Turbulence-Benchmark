
def return_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    result = []
    for i in range(1, 7):
        if string[i] in vowels and string[i].upper() >= "F" and string[i].upper() <= "j":
            result.append(string[i])
    return result
