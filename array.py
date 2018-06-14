#For two arrays of data, sort it so that one array data 
#is from smallest to the biggest value, the other array 
#is from the biggest to the smallest.
def bubbleSort(array,indicator):
    for passnum in range(len(array)-1,0,-1):
        for i in range(passnum):
	        if indicator == 0:    
	            if array[i]>array[i+1]: # Sort from low to high
	                temp = array[i]
	                array[i] = array[i+1]
	                array[i+1] = temp
	        elif indicator == 1:
	            if array[i]<array[i+1]: # Sort from high to low
	                temp = array[i]
	                array[i] = array[i+1]
	                array[i+1] = temp
	        else:
	        	raise AssertionError('indicator must have int value of 0 or 1')



def main():
	array = [54,26,93,17,77,31,44,55,20]
	array1 = [100,4,78,98,30,20,21,21,0,5]
	bubbleSort(array,0) # 0 indicator means sorting array from low to high
	bubbleSort(array1,1) # 1 indicator means sorting array from high to low
	
	print(array, end=' --> ')
	print('array data from smallet to biggest value')
	
	print(array1, end=' --> ')
	print('array1 data from biggest to smallest value')

if __name__ == '__main__':
	main()