def binary_search(arr, target):
    comparisons = 0
    left, right = 0, len(arr) - 1

    while left <= right:
        comparisons += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return comparisons


def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            return False
    return True


def main():
    with open('input', 'r') as file:
        array = [int(x) for x in file.read().split(' ')]
    if not is_sorted(array):
        print("Массив должен быть отсортирован по возрастанию")
        return
    n = len(array)
    total_comparisons = 0

    with open('output', 'w') as output_file:

        for target in array:
            comparisons = binary_search(array, target)
            total_comparisons += comparisons
            output_file.write(f"Искомое значение {target}: Кол-во сравнений = {comparisons}\n")

        output_file.write(f"Общее число сравнений = {total_comparisons}\n")
        output_file.write(f"A(N) = {total_comparisons / n}\n")


if __name__ == '__main__':
    main()
