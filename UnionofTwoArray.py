#Day 1: Problem 3: Given two arrays a[] and b[] of size n and m respectively. The task is to find the number of elements in the union between these two arrays.

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        set_a=set(a)
        set_b=set(b)
        union_set=set_a.union(set_b)
        return (len(union_set))
        '''merged=a+b
        merged.sort()
        count=1
        for i in range(1,n+m):
            if merged[i]!=merged[i-1]:
                count+=1
        return count'''
#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n,m=[int(x) for x in input().strip().split()]
        
        a=[int(x) for x in input().strip().split()]
        b=[int(x) for x in input().strip().split()]
        ob=Solution()
        
        print(ob.doUnion(a,n,b,m))
# } Driver Code Ends
