
def palindromes_of_specific_lengths(string):
    def is_palindrome(word):
        return word == word[::-1]

    result = set()
    substring = string[16:95].lower()
    
    for length in range(39, 53):
        for start in range(len(substring) - length + 1):
            segment = substring[start:start + length]
            if segment.isalpha() and is_palindrome(segment):
                result.add(segment)

    return result
