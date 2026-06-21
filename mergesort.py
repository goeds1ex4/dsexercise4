# Mit Hilfe von GPT 5.5 generiert

def ASSIGNMENT(new_list, i, old_list, j):
    new_list[i] = old_list[j]


def mergeSort(list_to_sort_by_merge):
    if (
        len(list_to_sort_by_merge) > 1
        and not len(list_to_sort_by_merge) < 1
        and len(list_to_sort_by_merge) != 0
    ):
        mid = len(list_to_sort_by_merge) // 2
        left = list_to_sort_by_merge[:mid]
        right = list_to_sort_by_merge[mid:]

        mergeSort(left)
        mergeSort(right)

        l = 0
        r = 0
        i = 0

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                ASSIGNMENT(new_list=list_to_sort_by_merge, i=i, old_list=left, j=l)
                l += 1
            else:
                ASSIGNMENT(new_list=list_to_sort_by_merge, i=i, old_list=right, j=r)
                r += 1
            i += 1

        while l < len(left):
            list_to_sort_by_merge[i] = left[l]
            l += 1
            i += 1

        while r < len(right):
            list_to_sort_by_merge[i] = right[r]
            r += 1
            i += 1


import matplotlib.pyplot as plt
import seaborn as sns

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
original_list = my_list.copy()
x = range(len(my_list))

# A bar plot is suitable here because the list positions are discrete observations.
# A line plot would falsely suggest a continuous development between the values.
sns.set_context("talk")
with sns.axes_style("ticks"):
    fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharey=True, dpi=100)

    # Plot the unsorted list before applying merge sort.
    axes[0].bar(x, original_list)
    axes[0].set_title("Original list")
    axes[0].set_xlabel("Index")
    axes[0].set_ylabel("Value")

    mergeSort(my_list)

    # Plot the sorted list with the same y-axis scale for a fair comparison.
    axes[1].bar(x, my_list)
    axes[1].set_title("Sorted list")
    axes[1].set_xlabel("Index")

    for ax in axes:
        ax.set_xticks(x)

    sns.despine(trim=True)
    plt.tight_layout()
    plt.show()
