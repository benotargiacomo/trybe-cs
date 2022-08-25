def quicksort(numbers):
    if len(numbers) <= 1:
        return numbers
    else:
        pivot = numbers.pop()

    higher = []
    lower = []

    for number in numbers:
        if number > pivot:
            higher.append(number)
        else:
            lower.append(number)

    return quicksort(higher) + [pivot] + quicksort(lower)


def is_anagram(first_string, second_string):
    first = list(first_string.lower())
    second = list(second_string.lower())

    first = quicksort(first)
    second = quicksort(second)

    if first == second:
        return True
    else:
        return False
