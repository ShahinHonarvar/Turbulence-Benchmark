
def return_n_greatest_chars(s):
    # sort the string in descending order based on ASCII value
    sorted_s = "".join(sorted(s, key=lambda x: ord(x), reverse=True))
    
    # create a list of 43 characters from the sorted string
    chars = sorted_s[:43]
    
    return chars
