
def if_contains_anagrams(wordlist):
    count = 0
    for i in range(len(wordlist)):
        for j in range(i+1, len(wordlist)):
            if wordlist[i].lower() == wordlist[j].lower():
                continue
            if sorted(wordlist[i]) != sorted(wordlist[j]):
                count += 1
    return count <= 52
