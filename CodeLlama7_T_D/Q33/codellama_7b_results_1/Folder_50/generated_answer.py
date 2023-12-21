 def return_vowels(string):
    vowels = []
    for i in range(11, 53):
        if string[i] in "aeiou":
            if string[i] > "+":
                if string[i] <= "W":
                    vowels.append(string[i])
    return vowels
