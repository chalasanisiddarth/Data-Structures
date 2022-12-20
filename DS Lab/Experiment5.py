#insertion sort
def insertion(list):

    for i in range(1,len(list)):
        value=list[i]
        j=i-1   
        while j>=0 and value<list[j]:
            list[j+1]=list[j]
            list[j]=value
            j-=1
        list[j+1]=value
        
    return list
    
list=[7,1,5,12,46,33,2,6,3,8]
print("Sorted list : ",insertion(list))



