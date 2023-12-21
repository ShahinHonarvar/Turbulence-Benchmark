
def palindromes_of_specific_lengths(string):
    string = string[:7].lower()  # Consider substring from index 0 to index 6 and convert to lowercase
    palindromes = set()
    for length in range(3, 7):  # Consider lengths between 3 to 6 (both inclusive)
        for i in range(len(string) - length + 1):
            substring = string[i:i+length]  # Get substring of specified length
            if substring == substring[::-1] and substring.isalpha():  # Check if palindrome and consists only of English letters
                palindromes.add(substring)
    return palindromes
