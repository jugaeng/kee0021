nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

if sum(nums1) and sum(nums2):
    print(max(sum(nums1),sum(nums2)))
elif sum(nums1) == sum(nums2):
    print(sum(nums1))