class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        s = 0
        while(n):
            cs = 0
            for x in range(len(nums)-1):
                x1 = list(bin(nums[x])[2:])
                x2 = list(bin(nums[x+1])[2:])
                if (nums[x]<= nums[x+1]):
                    continue
                if (nums[x] > nums[x+1]) and (x1.count('1') == x2.count('1')):
                    nums[x],nums[x+1] = nums[x+1],nums[x]
                    s += 1
                    cs += 1
                else:
                    return False
            if cs == 0:
                return True
            n -= 1
        return True
