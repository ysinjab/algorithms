using System;
using System.Numerics;

namespace csharp
{
    static class Karatsuba
    {
        public static BigInteger multiply(BigInteger x, BigInteger y)
        {
            int n = Math.Max(countBits(x), countBits(y));
            if (n <= 10)
            {
                return x * y;
            }
            else
            {
                n = (n / 2) + (n % 2);
                BigInteger b = x >> n;
                BigInteger a = x - (b << n);
                BigInteger d = y >> n;
                BigInteger c = y - (d << n);

                BigInteger ac = multiply(a, c);
                BigInteger bd = multiply(b, d);
                BigInteger abcd = multiply(a + b, c + d);
                BigInteger x1 = (bd << 2 * n);
                BigInteger x2 = ((abcd - ac - bd) << n);
                return ac + x1 + x2;
            }
        }
        public static int countBits(BigInteger number)
        {
            return (int)Math.Log((double)number, 2.0) + 1;
        }
    }
}
