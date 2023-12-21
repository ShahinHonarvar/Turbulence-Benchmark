
def palindromes_of_specific_lengths(string):
    # Split the string into a list of substrings
    substrings = [string[i:j+1] for i in range(13, 96) for j in range(i, 95) if string[i:j+1].lower() == string[i:j+1][::-1].lower()]
    # Filter the substrings to only include palindromes of lengths between 57 and 60 (both inclusive)
    palindromes = [substring for substring in substrings if len(substring) >= 57 and len(substring) <= 60]
    return set(palindromes)
