def problem1480():

    #My Solution:
    class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if i == 0:
                pass
            else:
                nums[i] = nums[i] + nums[i-1]
        return nums
    
    #Optimal Solution
    class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        return nums

    #Difference in approach
    #   I definied the base case of 1 unit array, whereas the optimal solution just incremented the step
    #   such that for loop is only accessed when length is greater than 1

def problem724():

    #My Solution:
    #   DNF

    #Optimal Solution:
    class Solution(object):
    def pivotIndex(self, nums):
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1

    #Difference in approach:
    #   I need to learn to use enumerate better

def problem217():

    #My Solution
    class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        duplicate = {}
        status = False
        
        for i, j in enumerate(nums):
            if j not in duplicate.values():
                duplicate[i] = j
            else:
                status = True
                break
        return status
    
    #Optimal Solution
    def containsDuplicate(self, nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)

    #Difference in approach:
    #   I do not know what set function is, I must learn it
    # https://leetcode.com/problems/contains-duplicate/discuss/1698064/5-Different-Approaches-w-Explanations