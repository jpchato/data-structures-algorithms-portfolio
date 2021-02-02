"""
Write a function called reverseArray which takes an array as an argument. Without utilizing any of the built-in methods available to your language, return an array with elements in reversed order.

Input	            Output

[1, 2, 3, 4, 5, 6]	[6, 5, 4, 3, 2, 1]

[89, 2354, 3546, 23, 10, -923, 823, -12]	[-12, 823, -923, 10, 23, 3546, 2354, 89]

"""

def reverseArray(array):
    reversed_array = []
    for item in range(len(array)):
        # print(item)
        x = array.pop()
        reversed_array.append(x)
    print(reversed_array)
    return reversed_array
    

if __name__ == "__main__":
    reverseArray([1, 2, 3, 4, 5, 6])