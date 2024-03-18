class Sprint:
    """
    Class to represent a sprint.

    Attributes:
        sprint_number (int): The number/identifier of the sprint.
        start_date (str): The start date of the sprint.
        end_date (str): The end date of the sprint.
        total_points (int): The total story points completed in the sprint.
    """

    def __init__(self, sprint_number, start_date, end_date):
        """
        Initializes a Sprint object with the given attributes.

        Args:
            sprint_number (int): The number/identifier of the sprint.
            start_date (str): The start date of the sprint.
            end_date (str): The end date of the sprint.
        """
        self.sprint_number = sprint_number
        self.start_date = start_date
        self.end_date = end_date
        self.total_points = []


class SprintManager:
    """
    Class to manage sprints and calculate velocity.

    Attributes:
        sprints (list): A list of Sprint objects representing the sprints.
    """

    def __init__(self):
        """
        Initializes a SprintManager object with an empty list of sprints.
        """
        self.sprints = []

    def accept_sprints_list(self, sprints):
        """
        Accepts a list of Sprint objects and sets it as the list of sprints for the SprintManager.

        Args:
            sprints (list): A list of Sprint objects representing the sprints.
        """
        self.sprints = sprints

    def calculate_total_points(self):
        """
        Calculates the total story points completed in each sprint.
        Updates the total_points attribute of each Sprint object.
        """
        for sprint in self.sprints:
            total_points = sum(sprint.total_points)
            sprint.total_points = total_points

    def calculate_average_velocity(self):
        """
        Calculates the average velocity across all sprints.

        Returns:
            float: The average velocity.
        """
        total_points = sum(sprint.total_points for sprint in self.sprints)
        num_sprints = len(self.sprints)
        return total_points / num_sprints if num_sprints > 0 else 0

    def output_average_velocity(self):
        """
        Outputs the average velocity.
        """
        average_velocity = self.calculate_average_velocity()
        print("Average Velocity:", average_velocity)


class TeamMember:
    """
    Class to represent a team member.

    Attributes:
        name (str): The name of the team member.
        hours_per_day (int): The number of hours the team member can work per day.
        vacation_days (int): The number of days off taken by the team member.
        ceremony_days (int): The number of days committed to Sprint ceremonies.
    """

    def __init__(self, name, hours_per_day, vacation_days, ceremony_days):
        """
        Initializes a TeamMember object with the given attributes.

        Args:
            name (str): The name of the team member.
            hours_per_day (int): The number of hours the team member can work per day.
            vacation_days (int): The number of days off taken by the team member.
            ceremony_days (int): The number of days committed to Sprint ceremonies.
        """
        self.name = name
        self.hours_per_day = hours_per_day
        self.vacation_days = vacation_days
        self.ceremony_days = ceremony_days

    def calculate_effort_hours(self, num_sprint_days):
        """
        Calculates the available effort-hours for the team member.

        Args:
            num_sprint_days (int): The number of days in the sprint.

        Returns:
            int: The available effort-hours for the team member.
        """
        if num_sprint_days <= 0:
            return 0
        
        total_days = num_sprint_days - self.vacation_days - self.ceremony_days
        return max(total_days * self.hours_per_day, 0)


class TeamEffortHourCalculator:
    """
    Class to calculate team effort-hour capacity.

    Attributes:
        team_members (list): A list of TeamMember objects representing the team members.
    """

    def __init__(self):
        """
        Initializes a TeamEffortHourCalculator object with an empty list of team members.
        """
        self.team_members = []

    def add_team_member(self, team_member):
        """
        Adds a TeamMember object to the list of team members.

        Args:
            team_member (TeamMember): The TeamMember object to be added.
        """
        self.team_members.append(team_member)

    def calculate_total_effort_hours(self, num_sprint_days):
        """
        Calculates the total available effort-hours for the team.

        Args:
            num_sprint_days (int): The number of days in the sprint.

        Returns:
            int: The total available effort-hours for the team.
        """
        total_effort_hours = sum(
            max(member.calculate_effort_hours(num_sprint_days), 0)
            for member in self.team_members
        )
        return total_effort_hours


# Sample usage:
if __name__ == "__main__":
    # Feature A - Calculate Sprint Velocity
    # Create Sprint objects
    sprint1 = Sprint(1, "2024-03-01", "2024-03-14")
    sprint1.total_points = [5, 8, 3]  # Example story points completed in sprint 1
    sprint2 = Sprint(2, "2024-03-15", "2024-03-28")
    sprint2.total_points = [7, 6, 4]  # Example story points completed in sprint 2

    # Create SprintManager object
    sprint_manager = SprintManager()

    # Accept list of Sprint objects
    sprint_manager.accept_sprints_list([sprint1, sprint2])

    # Calculate total points for each sprint
    sprint_manager.calculate_total_points()

    # Output average velocity
    sprint_manager.output_average_velocity()

    # Feature B - Calculate Team Capacity
    # Create team members
    member1 = TeamMember("Anisha", 8, 1, 1)
    member2 = TeamMember("Anshul", 7, 2, 1)

    # Create TeamEffortHourCalculator object
    calculator = TeamEffortHourCalculator()

    # Add team members to the calculator
    calculator.add_team_member(member1)
    calculator.add_team_member(member2)

    # Calculate total effort-hours for the team (assuming a 10-day sprint)
    total_effort_hours = calculator.calculate_total_effort_hours(10)
    print("Total Effort-minute for the Team:", total_effort_hours)