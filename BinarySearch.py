# DAY-1: Problem 1: Binary Search: Given a sorted array of size N and an integer K, find the position(0-based indexing) at which K is present in the array using binary search.
class Solution:	
	def binarysearch(self, arr, n, k):
		left=0
		right=n-1
		while left<= right:
		    mid = (right+left)//2
		    if arr[mid]==k:
		        return mid
		    elif arr[mid]<k:
    		    left=mid+1
    		else:
    		    right=mid-1
		return -1 
#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int, input().strip().split(' ')))
        k=int(input())
        ob = Solution()
        print (ob.binarysearch(arr, n, k))
# } Driver Code Ends
