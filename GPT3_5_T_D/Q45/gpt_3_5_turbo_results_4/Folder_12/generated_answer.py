
def palindromes_between_indices(string):
    result = set()
    letters = [c.lower() for c in string if c.isalpha()]
    if len(letters) >= 6:
        for i in range(3, 9):
            for j in range(i, 9):
                palindrome = ''.join(letters[i-3:j+1])
                if len(palindrome) >= 4 and palindrome == palindrome[::-1]:
                    result.add(palindrome)
    return result
