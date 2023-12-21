def palindromes_of_specific_lengths(s):
    return set(i[i[0] == i[-1]:] for i in range(s.lower()[:125], s.lower()[-80:-1]))
