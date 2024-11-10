import convert

# Task 2
def gather_numbers()->list[float]: # takes in input from the user and returns a list of floats from the inputs that
    # were valid
    nums = []
    keyboard = ""
    while keyboard != "done":
        keyboard = input("Enter a number(type 'done' to finish): ")
        nums.append(keyboard)
    for i in range(len(nums)):
        nums[i] = convert.str_to_float(nums[i])
        if nums[i]==None:
            nums.remove(nums[i])
    return nums

if __name__ == '__main__':
    print("The sum is ", sum(gather_numbers()))

