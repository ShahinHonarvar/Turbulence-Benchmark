
def return_vowels(string):
    vowels = ('a','e','i','o','u','A','E','I','O','U')
    sub_string = string[28:76]
    vowel_list = [char for char in sub_string if char in vowels and '+' < char <= 'z']
    return vowel_list
