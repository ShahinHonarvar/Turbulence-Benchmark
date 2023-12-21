
def return_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    result = []
    for i in range(464, 574):
        if string[i].lower() in vowels and string[i] <= "g":
            result.append(string[i])
    return result
