def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False
    if low_index >= high_index:
        return True
    if word[low_index] != word[high_index]:
        return False
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)

# def is_palindrome_recursive(word):
#     if len(word) <= 1:
#         return True
#     else:
#         return word[0] == word[-1] and is_palindrome_recursive(word[1:-1])
    