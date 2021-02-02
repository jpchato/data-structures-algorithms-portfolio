'''
Feature Tasks
Write a function called BinarySearch which takes in 2 parameters: a sorted array and the search key. Without utilizing any of the built-in methods available to your language, return the index of the array’s element that is equal to the search key, or -1 if the element does not exist.
NOTE: The search algorithm used in your function should be a binary search.
Check the Resources section for details
Example
Input	Output
[4,8,15,16,23,42], 15	2
[11,22,33,44,55,66,77], 90	-1
[1, 2, 3, 5, 6, 7], 4	-1
'''
# incorrect solution --- does not use binary search, iterates through the whole array
def binary_search(sorted_array, search_key):
    for i in range(len(sorted_array)):
        if sorted_array[i] == search_key:
            print(sorted_array[i])
            print(i)
            return i
        elif search_key not in sorted_array:
            print(-1)
            return -1
            
if __name__ == "__main__":
    binary_search([4,8,15,16,23,42], 15)
    binary_search([11,22,33,44,55,66,77], 90)
    binary_search([1, 2, 3, 5, 6, 7], 4)