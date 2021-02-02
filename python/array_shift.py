'''
Feature Tasks

Write a function called insertShiftArray which takes in an array and the value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.

Example

Input	Output
[2,4,6,8], 5	[2,4,5,6,8]
[4,8,15,23,42], 16	[4,8,15,16,23,42]
'''
import math

def insert_shift_array(array, value):
    # middle_index = (len(array)//2)
    middle_index = math.ceil(len(array)/2)
    end_piece = array[middle_index:len(array)]
    start_piece = array[0:middle_index]
    start_piece.append(value)
    for item in end_piece:
        start_piece.append(item)
    print(start_piece)
    


if __name__ == "__main__":
    insert_shift_array([2,4,6,8], 5)
    insert_shift_array([4,8,15,23,42], 16)