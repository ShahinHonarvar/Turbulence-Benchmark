
def all_right_truncatable_prime(t):
    def is_prime(n):
        if n<=1:
            return False
        if n==2: 
            return True
        if n%2==0: 
            return False
        for current in range(3, int(n ** 0.5) + 1, 2):
            if n % current == 0: 
                return False
        return True

    def is_right_truncatable(x):
        x_str = str(x)
        while len(x_str) > 1:
            x_str = x_str[:-1]
            if not is_prime(int(x_str)):
                return False
        return True

    rtp = []
    for i in range(t[0]-1,1,-1):
        if is_prime(i) and is_right_truncatable(i):
            rtp.append(i)
    return sorted(rtp, reverse = True)
