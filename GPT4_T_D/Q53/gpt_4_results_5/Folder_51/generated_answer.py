
def palindrome_of_length_at_least_n(st):
    palindrome_set = set()
    st = ''.join(filter(str.isalpha, st)).lower()
    for i in range(len(st)):
        for j in range(i+63, len(st)+1):
            if st[i:j] == st[i:j][::-1]:
                palindrome_set.add(st[i:j])
    return palindrome_set
