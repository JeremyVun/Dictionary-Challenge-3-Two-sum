def fast(nums, target):
  dictionary = {}
  for i in range(len(nums)):
    num = nums[i]
    if num in dictionary:
      return [dictionary[num], i]
    else:
      difference = target - num
      dictionary[difference] = i