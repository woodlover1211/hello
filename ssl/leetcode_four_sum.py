from typing import List


class LeetCode:
    def four_sum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        for k in range(n):
            cur = nums[k]
            # 第一层去重
            if k > 0 and cur == nums[k-1]:
                continue
            # 第一层剪枝
            # if 0 < target < cur:
            #     break
            for i in range(k+1, n):
                # 第二层去重
                temp = nums[i]
                if i > k+1 and temp == nums[i-1]:
                    continue
                # 定义双指针, 遍历数组寻找其余两个元素
                l = i + 1
                r = n - 1
                while l < r:
                    total = cur + temp + nums[l] + nums[r]
                    if total > target:
                        # r左移动
                        r -= 1
                    elif total < target:
                        # l右移动
                        l += 1
                    else:
                        # 加入结果
                        ans.append([cur, temp, nums[l], nums[r]])
                        # nums[l] 去重
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        # nums[r] 去重
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
        return ans


leet_code = LeetCode()
nums = [1, 0, -1, 0, -2, 2]
ans = leet_code.four_sum(nums, 0)
print(ans)



