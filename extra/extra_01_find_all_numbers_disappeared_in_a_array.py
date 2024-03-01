# 時間計算量 O(n^2)、空間計算量 O(n)
class Step1:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(1, len(nums)+1):
            # in は線形探索
            if i not in nums:
                ans.append(i)
        return ans

# 時間計算量 O(n)、空間計算量 O(n)
class Step2:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        appeared = [False] * (len(nums))
        ans = []
        for num in nums:
            appeared[num-1] = True 
        for i in range(len(appeared)):
            if not appeared[i]:
                ans.append(i+1)
        return ans

# 時間計算量 O(n)、空間計算量 O(1)
# 出現した値をインデックスとする値をマイナスにする
class Advanced:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            abs_num = abs(num)
            if nums[abs_num-1] > 0:
                nums[abs_num-1] *= (-1)
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i+1)
        return ans


        
            
        


        
            
        