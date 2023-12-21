def all_left_truncatable_prime(test_case):
    # Your code here
    prime = []
    left_ truncatable = []
    for i in range(2, test_case[0]):
        if prime[i]:
            left_truncatable.append(i)
        for j in range(2, i):
            if prime[i]:
                prime[i] = False
                if prime[j]:
                    left_truncatable.append(j)
                prime[i] = True
    left_truncatable.sort(reverse=True)
    return left_trunc truncatable
