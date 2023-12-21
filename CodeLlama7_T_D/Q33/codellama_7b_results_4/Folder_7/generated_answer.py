 def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 202
    end_index = 872
    char_3 = my_string[2]
    char_4 = my_string[3]
    filtered_vowels = []
    for vowel in vowels:
        if (vowel > char_3) and (vowel <= char_4):
            filtered_vowels.append(vowel)
    return filtered_vowels
