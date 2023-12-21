
def return_vowels(string):
    result = [char for char in string[483:664] if char > '&' and char <= 'h' and char in 'aeiouAEIOU']
    return result
