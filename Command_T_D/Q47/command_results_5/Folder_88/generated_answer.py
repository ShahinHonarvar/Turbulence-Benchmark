def palindromes_of_specific_lengths(s):
    return set(s[11:-11].lower() for i in range(11,87+1) if i >=11 and i <=87 and len(s[11:i]) == 4 or len(s[11:i]) == 5)
