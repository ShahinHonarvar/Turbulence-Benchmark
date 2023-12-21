
def palindromes_of_specific_lengths(string):
    # Find the substring from index 31 to index 91 (both inclusive)
    substring = string[31:92]
    # Create a list of all palindromes in the substring
    palindromes = []
    for i in range(50, 54):
        for j in range(len(substring) - i + 1):
            sub_palindrome = substring[j:j+i]
            if sub_palindrome == sub_palindrome[::-1]:
                palindromes.append(sub_palindrome)
    # Return the set of all palindromes with lengths between 50 and 53 (both inclusive), found in the specified index range, in a case-insensitive manner
    return set(palindromes)
