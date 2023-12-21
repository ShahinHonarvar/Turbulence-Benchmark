
def return_vowels(my_string):
    # Create a list of all vowel letters in the specified range
    vowel_list = []
    for char in my_string[19:20]:
        if char.isalpha() and char.lower() in "aeiou":
            vowel_list.append(char)
    return vowel_list
