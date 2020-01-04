import timeit 

TEST_CODE = ''' 
from karatsuba import karatsuba
karatsuba(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627)
'''
# timeit.repeat statement 
times = timeit.repeat(stmt = TEST_CODE, 
                        repeat = 3, 
                        number = 1000) 
  
print(min(times))
#0.580346107483

TEST_CODE = ''' 
3141592653589793238462643383279502884197169399375105820974944592 * 2718281828459045235360287471352662497757247093699959574966967627
'''
times = timeit.repeat(stmt = TEST_CODE, 
                        repeat = 3, 
                        number = 1000) 
  
print(min(times))
#1.50203704834e-05