print("Hello world")

#Q2
import itertools

n = int(input())
bar = list(map(int,input().strip().split()))[:n]

def weld(bar):
    possible = []
    for i in range(len(bar)):
        this_bar = bar[i]
        other_bar = bar[:i] + bar[i+1:]
        for j in range(1, len(other_bar)+1):
            j_comb = list(itertools.combinations(other_bar, j))
            for this_set in j_comb:

                if sum(list(this_set)) == this_bar:
                    possible.append(this_bar)
    if possible == []:
        return 0                
    else:
        return max(possible)

print(weld(bar))
