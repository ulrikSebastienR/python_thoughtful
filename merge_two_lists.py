l1 = [char for char in "abcdefghijklmn"]
l2 = [char for char in "0123456789"]
#INTENDED OUTPUT = "aBcDe" DONE



l = []
i = len(l1) if len(l1) < len(l2) else len(l2)
for j in range(i):
    l.append(l1[j] if j%2 == 0 else l2[j])

#INTENDED OUTPUT = a0b1c2--i9jklmn DONE

l_extended = []
i_big = len(l1) if len(l1)>len(l2) else len(l2)

for j in range(i_big):
    if j < i:
        l_extended.append(l1[j])
        l_extended.append(l2[j])
    else:
        l_extended.append(l1[j])
    

#INTENDED OUTPUT = a9b8 DONE
l_mixed = []        
for j in range(i):
    l_mixed.append(l1[j] if j%2==0 else l2[i-j])

#INTENDED OUTPUT = a9b8j0klmn DONE
l_rev = []
for j in range(i_big):
    if j < i:
            l_rev.append(l1[j])
            l_rev.append(l2[i-1-j])
    else:
            l_rev.append(l1[j])
	


#INTENDED OUTPUT = a9b8--i0nmlkj
l_1rev = []

for j in range(i_big):
    if j < i:
        l_1rev.append(l1[j])
        l_1rev.append(l2[i-1-j])  
for k in range(i_big-i):
    l_1rev.append(l1[i_big-1-k])
   



for j in range(len(l)-1, 0,  -1):
    print(l[j])

    
    
