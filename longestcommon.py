def longestCommonSubsequence(text1, text2):
    t1 = len(text1)
    t2 = len(text2)
    L = [[0]*(t2+1) for i in range(t1+1)]
    for i in range(t1+1):
        for j in range(t2+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif text1[i-1] == text2[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    
    return L[t1][t2]