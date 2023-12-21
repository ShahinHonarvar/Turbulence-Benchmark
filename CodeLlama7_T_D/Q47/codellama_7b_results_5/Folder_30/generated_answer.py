
def palindromes_of_specific_lengths(string, start=14, end=90):
    # Create a list of all substrings in the specified range
    substrings = [string[i:j+1] for i in range(start) for j in range(i+end-start+1)]
    # Filter out substrings that are not palindromes or do not meet the length criteria
    palindromes = [s for s in substrings if s == s[::-1] and len(s) >= 55 and len(s) <= 71]
    return set(palindromes)
