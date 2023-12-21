
def palindromes_between_indices(string):
    letters = [char.lower() for char in string[7:10] if char.isalpha()]
    palindromes = set()

    if len(letters) < 3:
        return palindromes

    def backtrack(temp, start):
        if len(temp) > 2:
            palindromes.add(''.join(temp))

        for i in range(start, len(letters)):
            temp.append(letters[i])
            backtrack(temp, i)
            temp.pop()

    backtrack([], 0)
    return palindromes
