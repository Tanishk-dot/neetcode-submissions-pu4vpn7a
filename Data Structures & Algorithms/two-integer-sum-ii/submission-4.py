class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) -1

        while left < right:
            complement = target - numbers[left]

            if numbers[right] == complement:
                return[left+1,right+1]
                break
            else:
                right -=1
            if left >= right:
                left += 1
                right = len(numbers) -1
                
            
        