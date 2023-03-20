# python3
import math

def build_heap(data):
    swaps = []
    #TODO: Creat heap and heap sort
    #try to achieve  O(n) and not O(n2)
    n = len(data)
    parent=math.floor(n/2)
    for i in range(parent,-1,-1):
        j=i
        while True:
            max=j
            left_child=2*j +1
            if left_child < n and data[max]<data[left_child]:
                max=left_child
            right_child=2*j +2
            if right_child < n and data[max]<data[right_child]:
                max=right_child
            if j != max:
                swaps.append((j, max))
                data[j],data[max]=data[max],data[j]
                j=max
            else:
                break



    return swaps


def main():
    #TODO : add input and corresponding checks
    #add another input for I or F
    inp=input()
    if inp=="I":
        n = int(input())
        data = list(map(int, input().split()))
    elif inp=="F":
        filename="/tests"+input()
        with open(filename,'r',encoding="utf-8") as f:
            n = int(f.readline().strip())
            data = list(map(int, f.readline().strip().split()))


    # first two tests are from keyboard, third test is from a file


    # input from keyboard

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data
    # and give back all swaps
    swaps = build_heap(data)

    #TODO: output how many swaps were made,
    if len(swaps)<4*n:
        print(len(swaps))
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    #print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
