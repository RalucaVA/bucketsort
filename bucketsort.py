import time
st = time.time()

def bucket_sort(array):
    largest = max(array)
    length = len(array)
    size = largest/length
 
    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(array[i]/size)
        if j != length:
            buckets[j].append(array[i])
        else:
            buckets[length - 1].append(array[i])
 
    for i in range(length):
        insertion_sort(buckets[i])
 
    result = []
    for i in range(length):
        result = result + buckets[i]
 
    return result
 
def insertion_sort(array):
    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1
        while (j >= 0 and temp < array[j]):
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = temp
import random 
dataset=[]
for i in range(499):
    #x=random.randrange(0, 30033)
    dataset.append(i)
dataset = [int(x) for x in dataset]
sorted_list = bucket_sort(dataset)
print(sorted_list)



et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')