floor_dict={0:[x+1 for x in range(14)]}
for a in range(int(input())):
         k= int(input())
         n= int(input())
         if k==0: print (n)
         for c in range(1,k):
             floor_dict[c]=[sum(floor_dict[c-1][:x+1]) for x in range (n)]      
         print(sum(floor_dict[k-1][:n]))
