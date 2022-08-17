# You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

# The lock initially starts at '0000', a string representing the state of the 4 wheels.

# You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

# Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

 

# Example 1:

# Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# Output: 6
# Explanation: 
# A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
# Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
# because the wheels of the lock become stuck after the display becomes the dead end "0102".
# Example 2:

# Input: deadends = ["8888"], target = "0009"
# Output: 1
# Explanation: We can turn the last wheel in reverse to move from "0000" -> "0009".
# Example 3:

# Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
# Output: -1
# Explanation: We cannot reach the target without getting stuck.

# bFS method:
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        if target == '0000':
            return 0
        if '0000' in deadends:
            return -1
        
        # Initial Queue
        que = collections.deque()
        visited = set()
        que.append('0000')
        visited.add('0000')
        count = 0
        

        # Starting BFS
        while que:
            # for each level
            for i in range(len(que)):
                cur = que.popleft()
                if cur in deadends:
                    continue
                if cur == target:
                    return count
                
                for j in range(4):
                    plusOne = cur[0:j] + ('0' if cur[j] == '9' else str(int(cur[j])+1)) + cur[j+1:]
                    minOne = cur[0:j] + ('9' if cur[j] == '0' else str(int(cur[j])-1)) + cur[j+1:]
                    if plusOne not in visited:
                        que.append(plusOne)
                        visited.add(plusOne)
                    if minOne not in visited:
                        que.append(minOne)
                        visited.add(minOne)
            count += 1
        return -1

