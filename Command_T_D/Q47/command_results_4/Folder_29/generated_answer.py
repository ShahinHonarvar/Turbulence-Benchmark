def palindromes_of_specific_lengths(s):
    # Your code here
    letters = set(str(i) for i in range(ord('a'), ord('z')+1))
    return {i[15:94] for i in s.lower() if i.count(i[::-1]) == 1 and len(i) in range(18, 74)}
