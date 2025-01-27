import random
import time

# This method partitions the array around a randomly chosen pivot element.
# The pivot is placed in its correct sorted position, and all elements
# smaller than the pivot are moved to its left, while all elements greater
# than the pivot are moved to its right.
def randomized_partition(array, start_index, end_index):
    pivot_index = random.randint(start_index, end_index)
    array[pivot_index], array[end_index] = array[end_index], array[pivot_index]
    pivot_value = array[end_index]
    smaller_element_index = start_index - 1

    for current_index in range(start_index, end_index):
        if array[current_index] <= pivot_value:
            smaller_element_index += 1
            array[smaller_element_index], array[current_index] = array[current_index], array[smaller_element_index]

    array[smaller_element_index + 1], array[end_index] = array[end_index], array[smaller_element_index + 1]
    return smaller_element_index + 1

#Actual method to start the sorting of data. Divides the data into two parts 
#and calls itself.
def randomized_quicksort(array, start_index, end_index):
    if start_index < end_index:
        pivot_index = randomized_partition(array, start_index, end_index)
        randomized_quicksort(array, start_index, pivot_index - 1)
        randomized_quicksort(array, pivot_index + 1, end_index)

#This method validates that the array is valid before calling quick sort
def quicksort_validated(array):
    # null val check just in case array is null or empty
    if array is None or len(array) == 0:
        return array

    randomized_quicksort(array, 0, len(array) - 1)
    return array

#method is used to print the time taken to execute the sorting.
def print_difference(start_time, end_time, data_type):
    print(f"Time taken for {data_type}: {end_time - start_time:.6f} seconds")

# This is array going from 1 to 10000.
sorted = list(range(1, 20001))

#This is an array going from 10000 to 1.
sorted_descending = list(range(20000, 0, -1))

#This is a random array of 10000 number. No duplicates allowed.
random_data = random.sample(range(1, 20001), 20000)

#This is a random array of 10000 numbers. They can range from 0 to 10000 but can have duplicates.
random_data_duplicate = random.choices(range(1, 20001), k=20000)


# The below code calls the quick sort and record the time taken to execute for each type of data.
#using sorted data type
start_time = time.time()
quicksort_validated(sorted)
end_time = time.time()
print_difference(start_time, end_time, "sorted data for randomized merge sort")

#using reverse sorted data type
start_time = time.time()
quicksort_validated(sorted_descending)
end_time = time.time()
print_difference(start_time, end_time, "reverse sorted data for randomized merge sort")

#using random data type
start_time = time.time()
quicksort_validated(random_data)
end_time = time.time()
print_difference(start_time, end_time, "Random data for randomized merge sort")

#using random data with duplicates
start_time = time.time()
quicksort_validated(random_data_duplicate)
end_time = time.time()
print_difference(start_time, end_time, "Random data with duplicates for randomized merge sort")
