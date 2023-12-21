
def palindromes_of_specific_lengths(string):
    # Define the range of indices for the substring
    start = 1
    end = 299
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each index in the range
    for i in range(start, end + 1):
        # Extract the substring starting at index i
        substr = string[i:]
        # Find all palindromes of lengths between 3 and 10 in the substring
        palindromes.update(p for p in substr if len(p) >= 3 and len(p) <= 10 and p == p[::-1]))
    return palindromes
