def palindromes_of_specific_lengths(s):
    return set(i[22:95] for i in s.lower() if i[22:95] == i[95:22])
