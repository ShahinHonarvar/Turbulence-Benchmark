def palindromes_of_specific_lengths(s):
    return {w for w in s[12:122].split("") if len(w) in range(12, 221) and set(w) <= set("qwertyuiopasdfghjklzxcvbnm")}
