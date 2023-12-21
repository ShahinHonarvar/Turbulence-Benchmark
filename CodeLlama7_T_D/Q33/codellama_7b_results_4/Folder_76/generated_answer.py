 def return_vowels(my_string):
    vowel_list = []
    for i in range(495, 837):
        if my_string[i].isalpha() and my_string[i].lower() in "aeiou":
            if my_string[i] > "B" and my_string[i] <= "t":
                vowel_list.append(my_string[i])
    return vowel_list
