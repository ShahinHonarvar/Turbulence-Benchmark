
def return_vowels(string):
    English_Vowels = 'aeiou'
    Vowels_in_String = [char for char in string[149:313] if char in English_Vowels and 'M' < char <= 'j']
    return Vowels_in_String
