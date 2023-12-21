 def return_vowels(my_string):
    vowel_list = []
    for i in range(142, 145):
        if my_string[i].isalpha() and my_string[i].lower() in ['a', 'e', 'i', 'o']:
            if my_string[i] > '4' and my_string[i] <= 'o':
                vowel_list.append(my_string[i])
    return vowel_list
