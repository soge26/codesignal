def solution(sequence):

    first = -10**5
    second = -10**5
    pos = 0
    count = 0

    while pos < len(sequence):
        if sequence[pos] > first:
            first = sequence[pos]
        elif sequence[pos] > second and sequence[pos] < first:
            second = sequence[pos]
        elif sequence[pos]<second or sequence[pos] = first:
            count+=1




solution([10, 1, 2, 3, 4, 5])
solution([1,2,1,2])
solution([3,4,1,4])