import numpy as np
result=[]
def rules(board,row,col):
    # check for if there exist an element in col
    for i in range (col):
        if board[row][i]==1:
            return False
     # check for if there exist an element in row
    for j in range (row):
        if board[j][col]==1:
            return False

    return True

def findsol(board,col):
    # print(len(board))
    if col==len(board): 
        v=[]
        counter=0
        for i in range(len(board)):
          for j in range(len(board)):
            if board[i][j] == 1:
              v.append(j+1)
              counter+=1
        if counter==len(board):
            result.append(v)
        return True
        
        return True
    for i in range(col,len(board)):
        for j in range(0,len(board)):
            if board[j][i]==0:
                if rules(board,j,i):
                    board[j][i]=1
                    res=findsol(board,i+1)
                    board[j][i]=0
                        
    return res



def main():
    n=int(input())
    while n:
        n-=1
        size=input()
        size=int(size)
        board=np.zeros((size,size),dtype=int)
        findsol(board,0)
        print(result[::-1])
        result.clear()
main()