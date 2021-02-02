"""
Write a function called reverseArray which takes an array as an argument. Without utilizing any of the built-in methods available to your language, return an array with elements in reversed order.

Input	            Output

[1, 2, 3, 4, 5, 6]	[6, 5, 4, 3, 2, 1]

[89, 2354, 3546, 23, 10, -923, 823, -12]	[-12, 823, -923, 10, 23, 3546, 2354, 89]

"""

def reverseArray(array):
    reversed_array = []
    for i in range(len(array)):
        reversed_array.append(array.pop())
    print(reversed_array)
    return reversed_array


if __name__ == "__main__":
    reverseArray([1, 2, 3, 4, 5, 6])
    reverseArray([89, 2354, 3546, 23, 10, -923, 823, -12])
    reverseArray([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]	)