def if_contains_anagrams(s):
    return sum(1 for i in range(len(s)) for j in range(i+1,len(s)) if str(s[i]).lower() == str(s[j]).lower()) <= 84
