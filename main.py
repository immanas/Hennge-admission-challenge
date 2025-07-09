def main():
    import sys
    import itertools  # Not used here, but often helpful for functional patterns

    # Step 1: Reading all input at once and split into tokens
    data = sys.stdin.read().split()
    def to_ints(lst): return tuple(map(int, lst))
    def process_case(data):
        if not data:
            return [], []

        # First element is X, rest are the numbers
        x, *rest = data
        x = int(x)
        nums, next_start = rest[:x], rest[x:]

        # If actual number of inputs doesn't match X, return error
        if len(nums) != x:
            return [-1], next_start

        try:
            nums = list(map(int, nums))
        except:
            return [-1], next_start

        #Raise to power 4 if number is ≤ 0
        def pow4(n): return n ** 4 if n <= 0 else 0

        #Sum of 4th powers of only non-positive numbers
        result = sum(map(pow4, nums))
        return [result], next_start

    #Recursively process all test cases
    def process_all(data, count, acc=[]):
        if count == 0 or not data:
            return acc
        result, remaining = process_case(data)
        return process_all(remaining, count - 1, acc + result)

    try:
        #Step 2: First value is total number of test cases
        total, *rest = data
        total = int(total)

        #Step 3: Process all test cases and get final output list
        output = process_all(rest, total)

        #Step 4: Printing final results, one per line
        print('\n'.join(map(str, output)))
    except:
        print(-1)


# only run main() if this is the top-level script
if __name__ == "__main__":
    main()
