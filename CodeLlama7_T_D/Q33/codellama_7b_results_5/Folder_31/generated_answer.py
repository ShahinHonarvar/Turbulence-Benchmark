 def return_vowels(string):
    vowels = []
    for i in range(65, 70):
        if string[i] > "%" and string[i] <= "G":
            vowels.append(string[i])
    return vowels
