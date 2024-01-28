#Day 1: Problem 4: You are given a string s. You need to reverse the string.

class Solution:
     def reverseWord(self, str: str) -> str:
        str2=''
        for i in range(len(str)-1,-1,-1):
            str2+=str[i]
        return str2
        
        '''
        # Possible Answer 2:
        return str[::-1]
        '''


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        ob = Solution()
        print(ob.reverseWord(s))
        t = t-1

# } Driver Code Ends
