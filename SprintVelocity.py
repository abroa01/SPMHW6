
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
