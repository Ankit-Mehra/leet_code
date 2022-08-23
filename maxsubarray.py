# def maxSubArray(nums: list[int]) -> int:
#     if len(nums) == 1:
#             return nums[0]
#     max_sum = sum(nums)
#     for i in range(len(nums)):
#         for f in range(i,len(nums)):
#             sum_now = sum(nums[i:len(nums)+(i-f)])
#             if max_sum < sum_now:
#                 max_sum = sum_now
#     return max_sum

#kadane's Algorithm
# local_maximum at index i is the maximum of A[i] and the sum of A[i] and 
# local_maximum at index i-1.
def maxSubArray(nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        local_sum,max_sum = nums[0],nums[0]
        for i in range(1,len(nums)):
            if local_sum >= 0 : 
                local_sum += nums[i]
            else: 
                local_sum =  nums[i]
            if local_sum > max_sum :
                max_sum = local_sum
        return max_sum


print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

    