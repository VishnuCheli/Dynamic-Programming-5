#Time Complexity:: O(m*n) - traversing all nodes in the grid
#Space Complexity:: O(m*n) - creating a grid and storing the lengths
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m = len(text1) #finding the length of the first text, let it be the rows
        n = len(text2) #finding the legnth of the second text, let it be the columns
        
        grid = [[0 for i in range(n+1)] for j in range(m+1)] #creating a grid using the found lengths(+1 is used to creat space to avoid boundary overflow)

        for i in range(m-1,-1,-1):  #starting the traversal from the bottom right of the grid
            for j in range(n-1,-1,-1): #traversing diagonally to the top left
                if text1[i]==text2[j]: #if the characters in the column and row match insert 1 + diagonal bottom right cells number
                    grid[i][j] = 1 + grid[i+1][j+1] 
                else:
                    grid[i][j] += max(grid[i][j+1], grid[i+1][j]) #if the row and column doesnt match add the max of subsequences length of the next cell on the bottom or right


        return grid[0][0] #the maximum length of a subsequence returned