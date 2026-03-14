class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sort_nums = sorted(nums)
        mapping = {}
        for i in range(len(sort_nums)):
            if sort_nums[i] not in mapping:
                mapping[sort_nums[i]] = i
        result = []
        for num in nums:
            result.append(mapping[num])
        return result

