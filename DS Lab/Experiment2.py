#binary search
def binary(list,element):

    list.sort()
    flag=0
    low=0
    high=len(list)-1

    #printing the sorted list
    print(list)

    while high>=low:
        mid=(low+high)//2
        if list[mid]==element:
            return mid
            flag+=1
            break
        elif element>list[mid]:
            low=mid+1
            high=high
        elif element<list[mid]:
            low=0
            high=mid-1
    
    if flag==0:
        return -1

element=int(input())
list=[3,8,66,143,9,8,10,56,2,9,0,1,12]
print(binary(list,element))