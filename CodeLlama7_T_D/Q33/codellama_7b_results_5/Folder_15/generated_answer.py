 def return_vowels(string):
    vowels = []
    for i in range(5, len(string)):
        if string[i] in "aeiou" and string[i-1] <= "^":
            if string[i] > "3":
                vowels.append(string[i])
    return vowels
