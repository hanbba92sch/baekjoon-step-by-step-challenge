testnum=int(input())



for _ in range(testnum):
    x,y=[int(x) for x in input().split()]
    N=1
    distance=y-x
    while True:
        if distance <=N**2:
            if distance < N**2-N+1:
                print(N*2-2)
            else:
                print(N*2-1)
            break
        N+=1
    
