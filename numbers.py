# Function 1: Calculate the sum
def sum_numbers(numbers):
    return sum(numbers)


# Function 2: Calculate the average (mean)
def average_numbers(numbers):
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)


# Function 3: Calculate the median and mode
def median_and_mode(numbers):
    if len(numbers) == 0:
        return None, None

    # Calculate median
    ordered = sorted(numbers)
    middle = len(ordered) // 2

    if len(ordered) % 2 == 0:
        median = (ordered[middle - 1] + ordered[middle]) / 2
    else:
        median = ordered[middle]

    # Calculate mode
    counts = {}

    for number in numbers:
        counts[number] = counts.get(number, 0) + 1

    mode = max(counts, key=counts.get)

    return median, mode


# Main program
numbers = [4, 2, 7, 2, 5]

print("Sum:", sum_numbers(numbers))
print("Average:", average_numbers(numbers))

median, mode = median_and_mode(numbers)

print("Median:", median)
print("Mode:", mode)