# We are given an array asteroids of integers representing asteroids in a row. The indices of the asteriod in the array represent their relative position in space.

# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.



# Example 1:
# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

# Example 2:
# Input: asteroids = [8,-8]
# Output: []
# Explanation: The 8 and -8 collide exploding each other.
# 
# Example 3:
# Input: asteroids = [10,2,-5]
# Output: [10]
# Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

asteroids = [5,10,-5]

def asteroidCollision(asteroids):
    stack = []

    for a in asteroids:
        # If a is moving right or stack is empty, just push it
        while stack and a < 0 < stack[-1]:
            # Collision: compare sizes
            if stack[-1] < -a:
                stack.pop()  # Right one is smaller, explode it
                continue
            elif stack[-1] == -a:
                stack.pop()  # Both same size, explode both
            break
        else:
            stack.append(a)

    return stack    


print(asteroidCollision(asteroids))