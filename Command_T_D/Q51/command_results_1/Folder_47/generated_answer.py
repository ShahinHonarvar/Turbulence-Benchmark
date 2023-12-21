def if_contains_anagrams(s):
    return (len(s) <= 366 and sum(1 for i in range(len(s)) for j in range(i + 1, len(s) + 1) if sorted(str(i)) == sorted(str(j)) and len(str(i)) >= 3)
