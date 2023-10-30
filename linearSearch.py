def linear_search(arr, target):
    comparisons = 0
    for num in arr:
        comparisons += 1
        if num == target:
            return comparisons
    return comparisons


def main():
    with open('input', 'r') as file:
        array = list(map(int, file.read().split(' ')))

    n = len(array)
    total_comparisons = 0

    with open('output', 'w') as output_file:
        for target in array:
            comparisons = linear_search(array, target)
            total_comparisons += comparisons
            output_file.write(f"Искомое значение {target}: Кол-во сравнений = {comparisons}\n")

        output_file.write(f"Общее число сравнений = {total_comparisons}\n")
        output_file.write(f"A(N) = {total_comparisons / n}\n")


if __name__ == '__main__':
    main()
