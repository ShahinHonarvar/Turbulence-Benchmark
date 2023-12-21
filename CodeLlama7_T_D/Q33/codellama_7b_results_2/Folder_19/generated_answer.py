
def return_vowels(string):
    vowels = []
    for i in range(51, 77):
        if string[i] in "aeiou":
            if string[i] > 4:
                if string[i] <= "=":
                    vowels.append(string[i])
    return vowels
