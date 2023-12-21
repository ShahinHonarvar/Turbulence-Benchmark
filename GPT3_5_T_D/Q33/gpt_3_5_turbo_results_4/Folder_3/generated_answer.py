
def return_vowels(string):
    vowels = []
    for i in range(50, 77):
        if "a" <= string[i] <= "r" and string[i] in "aeiou":
            vowels.append(string[i])
    return vowels
