def sum_numbers(numbers):
    """Return the sum of the numbers."""
    return sum(numbers)


def average_numbers(numbers):
    """Return the average, or None if the list is empty."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


def median_and_mode(numbers):
    """Return the median and mode. For ties, return the first mode found."""
    if not numbers:
        return None, None

    ordered = sorted(numbers)
    middle = len(ordered) // 2

    if len(ordered) % 2 == 0:
        median = (ordered[middle - 1] + ordered[middle]) / 2
    else:
        median = ordered[middle]

    counts = {}
    for number in numbers:
        counts[number] = counts.get(number, 0) + 1

    mode = max(counts, key=counts.get)
    return median, mode


# Example
numbers = [4, 2, 7, 2, 5]

print("Sum:", sum_numbers(numbers))
print("Average:", average_numbers(numbers))

median, mode = median_and_mode(numbers)
print("Median:", median)
print("Mode:", mode)