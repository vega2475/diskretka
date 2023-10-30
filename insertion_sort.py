def insertion_sort(arr):
    comparisons = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return comparisons + len(arr) - 1


def main():
    with open('input', 'r') as file:
        array = [int(x) for x in file.read().split(' ')]

    comparisons = insertion_sort(array)

    with open('output', 'w') as output_file:
        output_file.write(" ".join(map(str, array)) + "\n")
        output_file.write(f"Число сравнений: {comparisons}\n")


if __name__ == '__main__':
    main()
