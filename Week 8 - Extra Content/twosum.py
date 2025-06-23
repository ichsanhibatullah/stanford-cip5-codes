def main():
    """
    Calls two_sum_finder on a few sample inputs.
    You can add more test cases here to check your work!
    """
    print(two_sum([2, 7, 11, 15], 9))     # Expected: True
    print(two_sum([1, 2, 3, 4], 8))       # Expected: False
    print(two_sum([5, 5], 10))            # Expected: True
    print(two_sum([4], 8))                # Expected: False

def two_sum(nums, target):
    """
    Returns True if any two distinct elements in the list `nums`
    add up to the value `target`. Otherwise, returns False.

    Examples:
    two_sum([2, 7, 11, 15], 9) -> True
    two_sum([1, 2, 3, 4], 8) -> False
    """
    # TODO: implement this function
    nums_len = len(nums)
    if nums_len == 1:
        if nums[-1] == target:
            return True
        else:
            return False
    
    for i in range(nums_len):
        num_besides_i = [] # skip if num == i
        for j in range(nums_len):
            if i != j:
                num_besides_i.append(j)
        
        for k in num_besides_i:
            if nums[i] + nums[k] == target:
                return True
        return False

if __name__ == '__main__':
    main()