
def palindromes_between_indices(string):
    letters = set(string[4:9])
    palindromes = []
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            if letters[j] == letters[i]:
                continue
            elif letters[j] < letters[i]:
                break
            else:
                palindrome = "".join([letters[k] for k in range(i, j+1)])
                if len(palindrome) >= 5 and palindrome == palindrome[::-1]:
                    palindromes.append(palindrome)
    return set(palindromes)
