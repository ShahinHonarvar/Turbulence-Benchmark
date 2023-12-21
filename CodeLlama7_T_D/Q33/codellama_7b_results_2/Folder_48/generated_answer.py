
def return_vowels(my_string):
    # Create a list of all vowel letters in the string
    vowel_list = []
    for char in my_string:
        if char in "AEIOUaeiou" and 529 <= ord(char) <= 828:
            vowel_list.append(char)
    return vowel_list
