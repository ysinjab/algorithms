def karatsuba(x,y):
    n = max(len("{0:b}".format(x)), len("{0:b}".format(y)))
    if (n <= 10):
        return x * y
    else:
        n = (n / 2) + (n % 2)
        b = x >> n
        a = x - (b << n)
        d = y >> n
        c = y - (d << n)
        
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        abcd = karatsuba(a + b, c + d)
        return ac + (bd << 2 * n) + ((abcd - ac - bd) << n)

print(karatsuba(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627))