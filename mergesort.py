"""Visualize an example list before and after sorting it with merge sort."""

import matplotlib.pyplot as plt
import seaborn as sns


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


def plot_values(original_values: list[int], sorted_values: list[int]) -> None:
    """Plot the values before and after sorting with comparable axes."""
    x_values = range(len(original_values))

    # A bar plot is suitable because list positions are discrete observations.
    # A line plot would falsely suggest continuous development between values.
    sns.set_context("talk")
    with sns.axes_style("ticks"):
        _, axes = plt.subplots(1, 2, figsize=(12, 5), sharey=True, dpi=100)

        # Plot the unsorted list before applying merge sort.
        axes[0].bar(x_values, original_values)
        axes[0].set_title("Original list")
        axes[0].set_xlabel("Index")
        axes[0].set_ylabel("Value")

        # Plot the sorted list with the same y-axis scale for a fair comparison.
        axes[1].bar(x_values, sorted_values)
        axes[1].set_title("Sorted list")
        axes[1].set_xlabel("Index")

        for ax in axes:
            ax.set_xticks(x_values)

        sns.despine(trim=True)
        plt.tight_layout()
        plt.show()


def main() -> None:
    """Plot the example list before and after sorting."""
    numbers = EXAMPLE_NUMBERS.copy()
    original_numbers = numbers.copy()

    merge_sort(numbers)
    plot_values(original_numbers, numbers)


if __name__ == "__main__":
    main()
