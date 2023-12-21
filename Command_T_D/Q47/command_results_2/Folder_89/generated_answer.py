def palindromes_of_specific_lengths(str1):
    str1 = str1[18:88].lower()
    return {x[::-1] for x in str1[11:-11:-1] if set(x) <= set("qwertyuiopasdfghjklzxcvbnm")}
