 def palindromes_of_specific_lengths(string):
    # create a substring from index 106 to index 280 (both inclusive)
    substr = string[106:281]
    # find all palindromes in the substring using a regular expression
    palindromes = re.findall(r"\b(\w+?)\b", substr, re.I)
    # filter out palindromes that are not of lengths between 136 and 151 (both inclusive)
    filtered_palindromes = [x for x in palindromes if len(x) >= 136 and len(x) <= 151]
    return set(filtered_palindromes)
