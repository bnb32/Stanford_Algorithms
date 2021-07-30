def merge(a,b):
    i=0;j=0;
    out=[0]*(len(a)+len(b))
    
    for k in range(0,len(a)+len(b)-1):
        if i==len(a) and (j+1)<len(b):
            out[k]=b[j]
            j+=1
        elif j==len(b) and (i+1)<len(a):
            out[k]=a[i]
            i+=1
        elif a[i]<b[j]:
            out[k]=a[i]
            i+=1
        elif b[j]<=a[i]:
            out[k]=b[j]
            j+=1

    out[-1]=max((a[-1],b[-1]))

    return out        

def mergeSort(a):
    left = a[0:len(a)//2]
    right = a[len(a)//2:]

    if min((len(left),len(right)))==1:
        
        left.sort()
        right.sort()
        
        return merge(left,right)

    else:

        return merge(mergeSort(left),mergeSort(right))

a=[1,3,2,10,8,5,11,6,13]

print(mergeSort(a))

#print(merge([1,3],[2,4]))
