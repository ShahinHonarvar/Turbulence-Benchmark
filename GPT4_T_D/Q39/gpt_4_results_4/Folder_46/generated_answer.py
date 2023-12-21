
def return_n_greatest_chars(given_string):
    
    sorted_string = sorted(given_string, key = ord, reverse = True)
    nth_greatest_chars = sorted_string[:54]
    
    return nth_greatest_chars
