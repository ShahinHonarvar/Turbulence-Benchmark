
def palindromes_of_specific_lengths(string):
    palindrome_set = set()
    for i in range(13, 74): #upper bound of 74 ensures max len palindrome is in range and less than 100.
        for length in range(26, 30): #upper bound of 30 as  range is exclusive.
            if i+length > 100:
                continue
            possible_palindrome = string[i:i+length]
            if not possible_palindrome.isalpha():
                continue
            if possible_palindrome.lower() == possible_palindrome[::-1].lower():
                palindrome_set.add(possible_palindrome)
    return palindrome_set
