def interpolation_search(arr, target):
    l = 0
    r = len(arr) - 1
    comparisons = 0

    while arr[l] < target < arr[r]:
        comparisons += 1
        if arr[l] == arr[r]:
            break
        index = (target - arr[l]) * (l - r) // (arr[l] - arr[r]) + l
        if arr[index] > target:
            r = index - 1
        elif arr[index] < target:
            l = index + 1
        else:
            return index, comparisons

    if arr[l] == target:
        return l, comparisons
    if arr[r] == target:
        return r, comparisons

    return -1, comparisons


def main():
    with open('input', 'r') as file:
        array = [int(x) for x in file.read().split(' ')]
    n = len(array)
    total_comparisons = 0

    with open('output', 'w') as output_file:
        for target in array:
            index, comparisons = interpolation_search(array, target)
            print(index)
            total_comparisons += comparisons
            output_file.write(f"Искомое значение {target}: Кол-во сравнений = {comparisons}\n")

        output_file.write(f"Общее число сравнений = {total_comparisons}\n")
        output_file.write(f"A(N) = {total_comparisons / n}\n")


if __name__ == '__main__':
    main()
