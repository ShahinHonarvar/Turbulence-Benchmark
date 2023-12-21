 def return_vowels(my_string):
    vowels = []
    for i in range(47, 61):
        if my_string[i].isalpha() and my_string[i].lower() in "aeiou":
            if my_string[i] > "9" and my_string[i] <= "O":
                vowels.append(my_string[i])
    return vowels
