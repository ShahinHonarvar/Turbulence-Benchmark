def palindromes_between_indices(s):
    # Write your code here
    for i in range(3,len(s)-2):
        for j in range(i+1,len(s)-2):
            if(s[i:j+1]==s[j:i+1]):
                yield s[i:j+1]
