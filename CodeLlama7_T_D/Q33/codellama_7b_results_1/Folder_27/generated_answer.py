 def return_vowels(my_string):
    vowels = []
    for i in range(29, 31):
        if my_string[i].lower() in "aeiou":
            if my_string[i].lower() > "a" and my_string[i].lower() <= "f":
                vowels.append(my_string[i])
    return vowels
