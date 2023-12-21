def find_sum_of_multiples(n):
    # Take input n from user
    if n<0:
        return -1
    if n<=85:
        return n*(n+1)/2
    else:
        return find_sum_of_multiples(n-1) + find_sum_of_multiples(n)
