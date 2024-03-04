
# Method to calculate average velocity
def calculate_average_velocity(sprints):
    """
    Calculate the average velocity given the points completed in previous sprints.

    Args:
        sprints (list of int): List of points completed in each sprint.

    Returns:
        float: Average velocity.
    """
    if not sprints:
        return 0
    total_points = sum(sprints)
    num_sprints = len(sprints)
    return total_points / num_sprints

# Method to get input for previous sprints point completion
def get_previous_sprints():
    """
    Get input for previous sprints point completion from the user.

    Returns:
        list of int: List of points completed in each sprint.
    """
    sprints = []
    num_sprints = int(input("Enter the number of previous sprints: "))
    for i in range(1, num_sprints + 1):
        points = int(input(f"Enter points completed in sprint {i}: "))
        sprints.append(points)
    return sprints
