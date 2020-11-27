class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        # My Solution
        sol = []
        for i in A:
            if i%2 == 0:
                sol.insert(0, i)
            else:
                sol.append(i)
        return(sol)
        
        # Not my solution
        # A.sort(key = lambda x: x%2)
        # return(A)