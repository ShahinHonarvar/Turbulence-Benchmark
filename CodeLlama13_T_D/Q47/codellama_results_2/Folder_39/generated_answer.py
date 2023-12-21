
def palindromes_of_specific_lengths(string):
    # Find all palindromes of lengths between 50 and 53 (both inclusive) in the substring from index 31 to index 91, both inclusive
    palindromes = {palindrome for i in range(31, 92) if len(palindrome) in range(50, 54) and palindrome == palindrome[::-1] for palindrome in string[i:i+len(string)-1]}
    return palindromes
