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

https://www.youtube.com/watch?v=DnvWAd-RGhk&ab_channel=DerrickSherrill
'''
# incorrect solution --- does not use binary search, iterates through the whole array
# def binary_search(sorted_array, search_key):
#     for i in range(len(sorted_array)):
#         if sorted_array[i] == search_key:
#             # print(sorted_array[i])
#             print(i)
#             return i
#         elif search_key not in sorted_array:
#             print(-1)
#             return -1

# def better_binary_search(sorted_array, search_key):
#     middle_index = round(len(sorted_array)/2)
#     middle_value = sorted_array[round(middle_index)]
#     print('middle index:', middle_index)
#     print('middle value:', middle_value)
#     print('search key:', search_key)
#     if search_key == middle_value:
#         print(middle_index)
#     index = round(middle_index)
#     print(index)
#     incrementing_index = middle_index
#     print(incrementing_index)
#     if search_key > middle_value:
#         print(sorted_array[incrementing_index + 1])

def binary_search(sorted_array, search_key):
    begin_index = 0
    end_index = len(sorted_array) - 1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index // 2)
        midpoint_value = sorted_array[midpoint]

        if midpoint_value == search_key:
            print(midpoint)
            return midpoint
        
        elif search_key < midpoint_value:
            end_index = midpoint - 1

        else:
            begin_index = midpoint + 1
    
    print(-1)
    return -1







    #     while incrementing_index < len(sorted_array) + 1:
    #         print('search key: ' + str(search_key) + ' is greater than the middle value:' + str(middle_value))
    #         incrementing_index = int(middle_index) + 1
    #         incremented_index_value = sorted_array[incrementing_index]
    #         print('incremented index value:', incremented_index_value)
    #         if incremented_index_value == search_key:
    #             print(search_key, incremented_index_value, index)
    #             return search_key, incremented_index_value, index
    #         elif index > len(sorted_array) + 1:
    #             print(-1)
    #             return -1
    # while search_key < middle_value:
    #     print('less')
    #     index = int(middle_index) - 1
    #     decremented_index_value = sorted_array[index]
    #     print(decremented_index_value)
    #     if decremented_index_value == search_key:
    #         print(search_key, decremented_index_value, index)
    #         return search_key, decremented_index_value, index
    #     elif index > len(sorted_array) - 1:
    #         print(-1)
    #         return -1


            
if __name__ == "__main__":
    binary_search([4,8,15,16,23,42], 15)
    binary_search([11,22,33,44,55,66,77], 90)
    binary_search([1, 2, 3, 5, 6, 7], 4)
    # better_binary_search([4,8,15,16,23,42], 15)
    # better_binary_search([11,22,33,44,55,66,77], 90)
    # better_binary_search([1, 2, 3, 5, 6, 7], 4)