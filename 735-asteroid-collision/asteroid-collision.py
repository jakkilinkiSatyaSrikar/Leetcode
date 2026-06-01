class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        # stack.append(asteroids[0])
        for i in asteroids:
            while stack and stack[-1]>0 and i<0:
                last = stack.pop()
                if(last>-(i)):
                    stack.append(last)
                    print("if",stack)
                    break
                elif last==-(i):
                    print("elif last==-(i)")
                    break
            else:
                stack.append(i)
        return stack