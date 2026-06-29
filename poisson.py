from numpy.random import exponential

# Get/set the parameters
intensity = 1
left_window_bound = 0
right_window_bound = 1

# Sample the wait times, compute points, and add them to a list
points = []
current_point = left_window_bound + exponential(1/intensity)
while(current_point <= right_window_bound):
    points.append(current_point)
    current_point += exponential(1/intensity)

# Print the list
print("Points:")
print(points)