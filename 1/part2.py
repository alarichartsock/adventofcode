"""The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?"""

import os
import time

def main():
    start = time.time()  
    f = open("input.txt",'r').read().split('\n') #turns file input into a list I can work with
    f.remove('') # removes any empty entries in the list
    f = f[:-1]
    f = list(map(int, f)) #turns every item in list into int for easier manipulation
    print(f)
    
    for i in f:
        for j in f:
            for k in f:
                if i+j+k == 2020:
                    print(i*j*k)    
    end = time.time()
    runtime = end - start
    print("Time " + str(runtime)) #Benchmarks solution

main() 
