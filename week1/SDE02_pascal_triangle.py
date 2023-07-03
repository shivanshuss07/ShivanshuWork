# pascal's Triangle =>  [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],...]
def printPascalTriangle(n):
    ans = [[1]]
    for i in range(n):
        temp = [0] + ans[-1] + [0]
        row = []
        for j in range(len(ans[-1])+1):
            row.append(temp[j] + temp[j+1])
        ans.append(row)
    print(ans)

printPascalTriangle(5)

# for specific element nCr or 11^r 
