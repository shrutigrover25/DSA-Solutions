class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:

        windowsum=0
        n=len(nums)

        for i in range(k):
            windowsum+=nums[i]

        averageSum=windowsum/k

        maxAverage=averageSum

        for i in range(k,n):
            windowsum+=nums[i]
            windowsum-=nums[i-k]

            averageSum=windowsum/k

            if averageSum>maxAverage:
                maxAverage=averageSum 


        return maxAverage
        