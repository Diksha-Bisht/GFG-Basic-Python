#Day 1: Problem 2: Power Of Two: Given a non-negative integer N. The task is to check if N is a power of 2. More formally, check if N can be expressed as 2x for some integer x. Return true if N is power of 2 else return false.

class Solution:
    ##Complete this function
    # Function to check if given number n is a power of two.
    def isPowerofTwo(self,n : int ) -> bool:
        if n==1:
            return True
        elif n==0 or n%2 !=0:
            return False
        else:
            n=n/2
            return self.isPowerofTwo(n)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        if ob.isPowerofTwo(n):
            print("YES")
        else:
            print("NO")
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
