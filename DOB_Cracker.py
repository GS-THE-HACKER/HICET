year='2003'
dict=[]
for j in range(5,13,1):
    l=str(j)
    if len(l)==1:
        l='0'+l
    for i in range(1,32,1):
        k=str(i)
        if len(k)==1:
            k='0'+k
        day_month=k+l
        #print(day_month+year)
        dict.append(day_month+year)
print(dict)
print(len(dict))