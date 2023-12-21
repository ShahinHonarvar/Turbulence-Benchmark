 def return_vowels(my_string):
    vowel_list = []
    for char in my_string[85:99]:
        if char.isalpha() and char.lower() in "aeiou":
            vowel_list.append(char)
    return vowel_list
