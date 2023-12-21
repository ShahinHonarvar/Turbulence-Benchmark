
def palindromes_of_specific_lengths(string):
    def check_palindrome(word):
        return word.lower() == word.lower()[::-1]

    result_set = set()
    substring = string[:6]

    for length in range(3, 6):
        for i in range(len(substring) - length + 1):
            chunk = substring[i:i + length]
            if chunk.isalpha() and check_palindrome(chunk):
                result_set.add(chunk)

    return result_set
