#Time Complexity:: O(n) - traversing all elements in the list twice(two times with start and end)
#Space Complexity:: O(1) - not creating any new datastructure
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0 #start pointer is created
        end = 0 #end pointer is created
        jumps = 0 #number of jumps counter
        while end<len(nums)-1: #while the end pointer hasn't reached the last number in the list
            farthest = 0 #the farthest is initiaized to zero
            for i in range(start,end+1): #the farthest jump point is calculated
                farthest = max(farthest,i+nums[i])

            jumps+=1 #the jump is incremented
            start = end+1 #the start pointer is moved beyond the end for the next jump
            end = farthest #end is moved to the farthest  the point reached so far
        return jumps #return the total jumps taken to reach te end of the list