from collections import defaultdict
d = defaultdict(list)
n,m = list(map(int,input().split()))
A = [d['A'].append(input()) for i in range(0,n)]
B = [d['B'].append(input()) for j in range(0,m)]
for i in range(0,len(d['B'])):
    result = [j+1 for j in range(0,len(d['A'])) if(d['B'][i] == d['A'][j])]
    if(result==[]):print(-1)
    else:print(*(result))
