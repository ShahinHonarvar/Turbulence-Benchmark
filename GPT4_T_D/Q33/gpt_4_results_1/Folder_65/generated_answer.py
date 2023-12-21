
def return_vowels(input_string):
    vowels = 'aeiou'
    sub_string = input_string[71:88]
    result = [char for char in sub_string if char in vowels and '9' < char.lower() <= 'p']
    return result
