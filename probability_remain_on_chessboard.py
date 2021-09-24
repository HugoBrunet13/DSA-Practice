# Python3 program to find the probability of
# the Knight to remain inside the chessboard
# after taking exactly K number of steps
# size of the chessboard 

def knightProbability(N: int, K: int, r: int, c: int) -> float:
    def dfs(N, K, i, j, dirs):
        if i < 0 or i >= N or j < 0 or j >= N: 
            return 0
        if K == 0:
            return 1
        rate = 0
        for di, dj in dirs:
            print("di: %s, dj: %s"%(di, dj))
            rec = dfs(N, K-1, i+di, j+dj, dirs) 
            print("dfs: ", rec)
            rate += 0.125 *  rec
            print("rate: ", rate)
        return rate
    
    dirs = [(-2,-1), (-2, 1), (-1,-2), (-1,2), (1,-2), (1,2), (2,-1), (2,1)]
    return dfs(N, K, r, c, dirs)


 
# Function Call
print(knightProbability(8, 1, 0, 0))