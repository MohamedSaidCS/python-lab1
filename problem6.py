def count_occurrences(string, char):
    count = 0
    for c in string:
        if char == c:
            count += 1
    return count


print(count_occurrences('google', 'o'))
