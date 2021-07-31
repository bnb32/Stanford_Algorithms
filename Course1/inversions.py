def mergeCountSplitInversions(a,b):
    i=0;j=0;count=0
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
            count+=(len(a[i:]))
            j+=1

    out[-1]=max((a[-1],b[-1]))

    return count,out        

def countInversions(a):
    count=0
    out=[0]*len(a)
    if len(a)==1: 
        count=0
        out=a[:]
    elif len(a)==2:
        if a[0]>a[1]: 
            count=1
            out[0]=a[1]
            out[1]=a[0]
        else:
            out=a[:]
    else:
        left=a[:len(a)//2]
        right=a[len(a)//2:]
        count_left,out_left=countInversions(left)
        count_right,out_right=countInversions(right)
        count_split,out=mergeCountSplitInversions(out_left,out_right)
        count=count_left+count_right+count_split
    
    return count,out

print(countInversions([3,5,1,2,4]))
