import re
def return_n_greatest_chars(s):
    # Find all unique characters in the string
    m = re.findall(r'[a-z]', s)
    
    # Sort the list of characters by ASCII value, then by occurrence
    m.sort(key=lambda x: (-x.lower(), s.count(x)))
    
    # Remove all but the first 39 characters
    return m[:39]
