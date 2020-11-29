maxCost = 19
s = "krrgw"
t = "zjxss"

j = 0
curCost = 0
res = 0
for i in range(len(s)):
    curCost += abs(ord(s[i])-ord(t[i]))
    while curCost > maxCost and j <= i:
        curCost -= abs(ord(s[j])-ord(t[j]))
        j += 1
    res = max(res, i-j+1)
print(res)
    
# print(abs(ord(s[i])-ord(t[i])))