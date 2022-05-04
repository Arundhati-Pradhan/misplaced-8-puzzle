def formatting(matrix):
    for i in range(9):
        if i%3==0 and i>0:
            print("")
        print(str(matrix[i])+" ", end = "")

def count(s):
    c = 0
    goal = [1, 2, 3,
             4, 5, 6,
             7, 8, 0]
    
    for i in range(9):
        if s[i]!=0 and s[i]!=goal[i]:
            c+=1
    return c


def move_place(ar, p, st):
    rh = 9999
    store_st = st.copy()
    
    for i in range(len(ar)):
        
        dupl_st = st.copy()
        
        tmp = dupl_st[p]
        dupl_st[p] = dupl_st[arr[i]]
        dupl_st[arr[i]] = tmp
        
        trh = count(dupl_st)
        
        if trh<rh:
            rh = trh
            store_st = dupl_st.copy()
    
    return store_st, rh
    
    
state = []
print("Enter your element: ")

for i in range(9):
    ele = int(input())
    state.append(ele) 
	
print("Start state: ", state)


h = count(state)


formatting(state)
print("\nMisplaced Heuristic Value : "+str(h))

print("")
print("->Solutions")


while h>0:
    position = int(state.index(0))
    
    
    if position==0:
        arr = [1, 3]
        state, h = move_place(arr, position, state)
    elif position==1:
        arr = [0, 2, 4]
        state, h = move_place(arr, position, state)
    elif position==2:
        arr = [1, 5]
        state, h = move_place(arr, position, state)
    elif position==3:
        arr = [0, 4, 6]
        state, h = move_place(arr, position, state)
    elif position==4:
        arr = [1, 3, 5, 7]
        state, h = move_place(arr, position, state)
    elif position==5:
        arr = [2, 4, 8]
        state, h = move_place(arr, position, state)
    elif position==6:
        arr = [3, 7]
        state, h = move_place(arr, position, state)
    elif position==7:
        arr = [4, 6, 8]
        state, h = move_place(arr, position, state)
    elif position==8:
        arr = [5, 6]
        state, h = move_place(arr, position, state)
        
    formatting(state)
    print("\nMisplaced Heuristic Value : "+str(h))
    
    
"""1
2
3
5
6
0
4
7
8"""
