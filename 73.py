class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0]) 
        m=len(matrix)   
        """
        Do not return anything, modify matrix in-place instead.
        """
        a=[]
        for i in range (m):
            for j in range (n):
                if matrix[i][j] == 0:
                    a.append([i,j])
                        
        for c,[i,j] in enumerate (a):
            #i,j=b
            for l in range (n):
                matrix[i][l]=0
            for k in range (m):
                matrix[k][j]=0