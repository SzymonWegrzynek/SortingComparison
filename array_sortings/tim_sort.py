def tim_sort(arr):
	min_run = 32
	n = len(arr)

	for i in range(0, n, min_run):
		insertion_sort(arr, i, min((i + min_run - 1), n - 1))

	size = min_run
	while size < n:
		for start in range(0, n, size * 2):
			mid = start + size - 1
			end = min((start + size * 2 - 1), (n - 1))
			merge(arr, start, mid, end)
		size *= 2

	return arr


def insertion_sort(arr, left, right):
	for i in range(left + 1, right + 1):
		key_item = arr[i]
		j = i - 1
		while j >= left and arr[j] > key_item:
			arr[j + 1] = arr[j]
			j -= 1
		arr[j + 1] = key_item


def merge(arr, start, mid, end):
    if start > mid or mid > end:
        return

    left = arr[start:mid + 1]
    right = arr[mid + 1:end + 1]

    left_idx, right_idx = 0, 0
    sorted_idx = start

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            arr[sorted_idx] = left[left_idx]
            left_idx += 1
        else:
            arr[sorted_idx] = right[right_idx]
            right_idx += 1
        sorted_idx += 1

    while left_idx < len(left):
        arr[sorted_idx] = left[left_idx]
        left_idx += 1
        sorted_idx += 1

    while right_idx < len(right):
        arr[sorted_idx] = right[right_idx]
        right_idx += 1
        sorted_idx += 1
