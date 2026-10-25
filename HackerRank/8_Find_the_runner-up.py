if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    nul=float('-inf')
    array=list(arr)
    for i in array:
        if i>nul:
            nul=i
    k=[]
    for j in array:
        if j==nul:
            continue
        k.append(j)
    w=float('-inf')
    for s in k:
            if s>w:
                w=s
    print(w)