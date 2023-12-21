
def return_vowels(string):
    vowels = 'aeiou'
    vowel_list = [char for char in string[50:77] if char in vowels and '#' < char <= 'r']
    return vowel_list
