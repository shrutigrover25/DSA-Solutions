class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        ## new window sum = old windowsum - element leaving+eleemnt 
        
        
        n=len(arr)
        
        ## create a first window 
        ## T.C : O(N)
        ## S.C : O(1)
        
        windowSum=0
        
        
        for i in range(k):
            windowSum+=arr[i]
            
        maxSum=windowSum
            
        
        ## slide the window 
        for i in range(k,n):
            windowSum+=arr[i]
            
            windowSum-=arr[i-k]
            
            maxSum=max(maxSum,windowSum)
            
        
        return maxSum