nums1 = [4,0,0,0,0,0]
nums2 = [1,2,3,5,6]
m = 1
n = 5

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    if m == 0:
        for i in range(n):
            nums1[i] = nums2[i]
    elif n == 0:
        pass
    else:
        i = 0 
        j = 0
        old_i = 0
        old_j = 0
        num1_gt_num2 = nums1[0] > nums2[0]
        result = []
        while j < n and i < m: 
            if num1_gt_num2:
                j += 1
                if j == n:
                    result += nums2[old_j:j] 
                    if len(nums1) - len(result) > 0:
                        result += nums1[i:i + len(nums1) - len(result)]
                    break
            else:
                i += 1
                if i == m:
                    result += nums1[old_i:i]
                    if len(nums1) - len(result) > 0:
                        result += nums2[j:j + len(nums1) - len(result)]
                    break
            
            if nums1[i] > nums2[j]:
                if not num1_gt_num2:
                    result = result + nums1[old_i:i]
                    old_i = i
                    
                num1_gt_num2 = True
                
            elif nums1[i] <= nums2[j]:
                if num1_gt_num2:
                    result = result + nums2[old_j:j]
                    old_j = j
                num1_gt_num2 = False
        
        for i, val in enumerate(result):
            nums1[i] = result[i]

merge(nums1, m, nums2, n)

print(nums1)