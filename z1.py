# import math
# import random
# import sys

# print "Jak dluga ma byc liczba:"
# x=raw_input()
# leading_zeroes=True
# if not leading_zeroes:
#     return random.randint(10**(x-1),10**x-1)
#   else:
#     if x>6000:
#       return ''.join([str(random.raindint(0,9))for i in xrange(x)])
#     else:
#       return '{0:0{x}d}'.format(random.randint(0,10**x-1),x=x)
# y=random.randrange(0,10**x)
# print(y)
import random

    leading_zeroes=True
    x=raw_input()
    if not leading_zeroes:
        # wrap with str() for uniform results
        return random.randint(10**(x-1), 10**x-1)  
    else:
        if x > 6000:
            return ''.join([str(random.randint(0, 9)) for i in xrange(x)])
        else:
            return '{0:0{x}d}'.format(random.randint(0, 10**x-1), x=x)
