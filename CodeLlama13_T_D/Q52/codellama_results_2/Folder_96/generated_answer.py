
def palindrome_of_length_n(string, n):
    # Use a regular expression to find all substrings of length 83 that are palindromes
    regex = r"[a-zA-Z]{%d}" % n
    matches = re.findall(regex, string)
    
    # Create a set to store the palindromes
    palindromes = set()
    
    # Iterate over the matches and add them to the set if they are palindromes
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
            
    return palindromes
