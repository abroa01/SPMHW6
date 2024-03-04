
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



if __name__ == "__main__":
    sprints = get_previous_sprints()
    average_velocity = calculate_average_velocity(sprints)
    output_average_velocity(average_velocity)
