#selection sort
def selection(list):

    for j in range(0,len(list)):
        min=j
        for i in range(j+1,len(list)):
            if list[i]<list[min]:
                temp=list[min]
                list[min]=list[i]
                list[i]=temp
        

    return list
    
        
list=[7,5,34,179,60,59,57,1]
print("Sorted list is : ", selection(list))

