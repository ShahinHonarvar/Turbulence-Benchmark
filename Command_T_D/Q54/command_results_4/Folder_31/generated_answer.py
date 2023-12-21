def all_right_truncatable_prime(n):
    # Write your code here.
    return [i for i in range(2, n[0] + 1) if all(str(i) in str(j) for j in range(2, int(str(i)[-1])))]
