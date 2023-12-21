
def palindromes_of_specific_lengths(string):
    # Define the substring of interest
    substr = string[18:98].lower()
    # Find all palindromes in the substring
    palindromes = [word for word in substr.split() if word == word[::-1]]
    # Filter out palindromes that do not meet the length requirement
    filtered_palindromes = []
    for palindrome in palindromes:
        if len(palindrome) in range(31, 52):
            filtered_palindromes.append(palindrome)
    return filtered_palindromes
