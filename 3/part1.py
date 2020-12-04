import os
import time
def main():
     start = time.time()  
     f = open("input.txt",'r').read().split('\n') # turns file input into a list I can work with

     for i in range(len(f)):
          f[i] = list(f[i])

     width = len(f[1])
     height = len(f)
     
     def traverse(dx,dy):
          finished = False
          treeCount = 0
          x = 0
          y = 0
          while(finished == False):
               if ( (x + dx) >= width):
                    x = (x + dx) % width
                    y = y + dy
               else:
                    x = x + dx
                    y = y + dy
               if(f[y][x] == '#'):
                    treeCount = treeCount + 1
               if (y+1  >= height):
                    finished = True
          return treeCount

     one = traverse(1,1)
     two = traverse(3,1)
     three = traverse(5,1)
     four = traverse(7,1)
     five = traverse(1,2)

     print(two)
     print(one*two*three*four*five)
     


     end = time.time()
     runtime = end - start
     print(runtime)

main() 
