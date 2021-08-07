"""
Merge Sort
"""

def merge_sort(lst: list) -> None:

    if len(lst) > 1:

        # find the middle of the list
        mid = len(lst)//2

        # divide the list into two stacks
        left_stack = lst[:mid]
        right_stack = lst[mid:]

        # recusive call each stack to keep splitting until we get single value stacks
        merge_sort(left_stack)
        merge_sort(right_stack)

        # index
        i = 0

        # look at the first value in each stack and take the lower until one stack is empty
        while left_stack and right_stack:
            if left_stack[0] < right_stack[0]:
                lst[i] = left_stack.pop(0)
            else:
                lst[i] = right_stack.pop(0)
            i += 1
 
        # get the rest of whichever stack was left
        while left_stack:
            lst[i] = left_stack.pop(0)
            i += 1
 
        while right_stack:
            lst[i] = right_stack.pop(0)
            i += 1


if __name__ == '__main__':
    lst = [9,8,7,6,5,4,3,2,1]
    print(f'Unsorted List:\t{lst}')
    merge_sort(lst)
    print(f'Sorted List:\t{lst}')
