'''
Given a list  [55,24,5,7,8,10]
write a function that will take this list and return it sorted
'''

# input is a list
# output is a sorted list
# visual
# [5, 7, 8, 10, 24, 55]
# algorithm
# list.insert(index_position, value)
# list.append(value) appends to the end of the list
# start, stop, step
def sorted_list(list_input):
    new_list = []
    while list_input:
        minimum = list_input[0]
        for item in list_input:
            if item < minimum:
                minimum = item
        new_list.append(minimum)
        list_input.remove(minimum)
    print(new_list)
    return new_list
        


if __name__ == "__main__":
    sorted_list([55,24,5,7,8,10])