# BUBBLE SORT
import time


def bubble_sort(numbs):
    if len(numbs) > 1:
        n =  len(numbs)-1
        while n >= 1:
            for i in range(n):
                if numbs[i] > numbs[i+1]:
                    temp = numbs[i]
                    numbs[i] = numbs[i+1]
                    numbs[i+1] = temp
            n -=1
    return numbs



def sort_lists (numb_set):
    if isinstance(numb_set, int) :  return numb_set
    elif (type(numb_set) != "list") :
        num_lis = list(numb_set)
        sorted_num_lst = bubble_sort(num_lis)
        return sorted_num_lst
    
    


set_of_lists = [(),(1, 2,5,3,1,7,9,1,12,83,1,5,3,2),\
(1,1,1,1,1,1,1,2,1,1,1), (2,2,2,2), (1,2), (2,1), (3)]

print("\n BUBBLE SORT")
input("")

for lst in set_of_lists:
    sorted_list = sort_lists(lst)
    print(f"before: {lst }")
    print(f"after: {sorted_list}\n")
    time.sleep(2)


 
