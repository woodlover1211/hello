from typing import List


class LeetCode:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        # 数组排序
        nums, ans = sorted(nums), []
        if n < 3: return []
        # 数组遍历
        for i in range(n - 2):  # 保证有三个元素
            # 第一个元素去重
            cur = nums[i]
            if i > 0 and nums[i] == nums[i - 1]: continue
            # 其余两个元素指针
            l = i + 1
            r = n - 1
            while l < r:
                total = cur + nums[l] + nums[r]
                if total == 0:
                    ans.append([cur, nums[l], nums[r]])
                    # 第二个元素去重，不断右移动
                    while l < r - 1 and nums[l] == nums[l + 1]:
                        l += 1
                    # 第三个元素去重，不断左移动
                    while l < r - 1 and nums[r] == nums[r - 1]:
                        r -= 1
                if total > 0:
                    # 左移动
                    r -= 1
                else:
                    # 右移动
                    l += 1
        return ans


nums = [-1, 0, 1, 2, -1, -4]
leet_code = LeetCode()
ans = leet_code.three_sum(nums)
print(ans)
