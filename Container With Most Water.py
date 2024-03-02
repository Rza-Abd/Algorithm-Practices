## 11. Container With Most Water
#You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
#Find two lines that together with the x-axis form a container, such that the container contains the most water.
#Return the maximum amount of water a container can store

max_volume = 0
left= 0
right= len(height) - 1

while left < right:
    volume = min(height[left], height[right]) * (right - left)
    max_volume = max(max_volume, volume)
    if height[left] < height[right]:
        left += 1
    else:
        right -= 1
    
# I use two pointers, one from left and one from right. 
# I calculate the volume of the container and compare it to the max_volume.
# If the volume is bigger, I update the max_volume.
# If the height of the left pointer is smaller than the height of the right pointer,