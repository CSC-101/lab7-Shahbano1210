import sys
import convert

def command_line_gather(s:list[str])->list[float]:  # takes in a list of the parameters in the configuration and
    # returns a new list of the values that were converted to float
    nums = []
    # convert sys values to float, sum, print
    for i in s[1:]:
        nums.append(i)
    for i in range(len(nums)):
        nums[i] = convert.str_to_float(nums[i])
        if nums[i]==None:
            nums.remove(nums[i])
    return nums



if __name__ == '__main__':
    print (sum(command_line_gather(sys.argv)))
