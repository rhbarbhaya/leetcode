class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        if (len(stones)-1) % (K-1) != 0:
            return(-1)
        sol = 0
#         while len(stones) != 1:
#             temp = []
#             for i in range(len(stones)-K+1):
#                 temp.append(sum(stones[i:K+i]))

#             idx = temp.index(min(temp))

#             for k in range(K):
#                 stones.pop(idx)

#             stones.insert(idx, min(temp))
#             sol += min(temp)
#             del temp[:]

#         return(sol)
        N = len(stones)
        if (N-1) % (K-1) != 0:
            return -1
        accum = [0] + list(itertools.accumulate(stones))

        dp = [[0]*N for _ in range(N)]
        for l in range(K, N+1):
            for i in range(N-l+1):
                j = i+l-1
                if l > K:
                    dp[i][j] = min([dp[i][t] + dp[t+1][j] for t in range(i,j,K-1)])
                if (l-1)%(K-1) == 0:
                    dp[i][j] += accum[j+1] - accum[i]

        return dp[0][N-1]