""" they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456

In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together? """

import os
import time

def main():
    start = time.time()  
    f = open("input.txt",'r').read().split('\n') # turns file input into a list I can work with
    f.remove('')
    f = f[:-1] #removes last item, the above line didn't remove it for some reason

    print(f)
    
    for i in range(len(f)):
        inputval = int(f[i])
        targetval = 2020 - inputval
        #print(str(targetval))
        if str(targetval) in f:
            result = inputval * targetval
            print("RESULT: " + str(result))   
    end = time.time()
    runtime = end - start
    print(runtime)

main() 
