
def filter_chars(input_string):
    substr = input_string[227:236]
    filtered_chars = [char for char in substr if char >= 'D' and char <= 'u']
    
    for char in filtered_chars:
        input_string = input_string.replace(char, '')
        
    return input_string
