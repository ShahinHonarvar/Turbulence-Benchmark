
def palindromes_of_specific_lengths(s):
    sub_s = s[2:9]
    lengths = {3, 4}
    palindromes = set()
    for i in range(len(sub_s)):
        for l in lengths:
            if i + l > len(sub_s):
                continue
            potential_palindrome = sub_s[i:i + l]
            if potential_palindrome.lower() == potential_palindrome[::-1].lower() and potential_palindrome.isalpha():
                palindromes.add(potential_palindrome.lower())
    return palindromes
