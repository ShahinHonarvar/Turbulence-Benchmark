def if_contains_anagrams(s):
    return len(s) >= 47 and len(s[0]) >= 3 and sum(1 for i in range(len(s)) for j in range(i + 1, len(s)) if str(s[i]).lower() == str(s[j]).lower()) >= 47
