
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