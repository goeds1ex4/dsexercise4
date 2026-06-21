#Mit Hilfe von GPT 5.5 erstellt

"""Visualize an example list before and after sorting it with merge sort."""

import matplotlib.pyplot as plt


EXAMPLE_NUMBERS = [54, 26, 93, 17, 77, 31, 44, 55, 20]


def merge_sort(values: list[int]) -> None:
    """Sort a list in ascending order in place using the merge sort algorithm.

    The function changes the input list directly and does not return a new list.
    It first splits the list into two halves, sorts both halves recursively, and
    then merges the sorted halves back into the original list.
    """
    if len(values) <= 1:
        return

    middle_index = len(values) // 2
    left_half = values[:middle_index]
    right_half = values[middle_index:]

    merge_sort(left_half)
    merge_sort(right_half)

    left_index = 0
    right_index = 0
    target_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] <= right_half[right_index]:
            values[target_index] = left_half[left_index]
            left_index += 1
        else:
            values[target_index] = right_half[right_index]
            right_index += 1

        target_index += 1

    while left_index < len(left_half):
        values[target_index] = left_half[left_index]
        left_index += 1
        target_index += 1

    while right_index < len(right_half):
        values[target_index] = right_half[right_index]
        right_index += 1
        target_index += 1


def plot_values(values: list[int]) -> None:
    """Plot the current order of the values."""
    x_values = range(len(values))
    plt.plot(x_values, values)
    plt.show()


def main() -> None:
    """Plot the example list before and after sorting."""
    numbers = EXAMPLE_NUMBERS.copy()

    plot_values(numbers)
    merge_sort(numbers)
    plot_values(numbers)


if __name__ == "__main__":
    main()
