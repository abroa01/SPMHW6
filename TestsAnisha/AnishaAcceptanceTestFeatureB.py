from SprintVelocity import TeamMember, TeamEffortHourCalculator
import unittest

class TestFeatureBAcceptance(unittest.TestCase):
    """
    Acceptance test class for Feature B (Calculate Team Effort-Hour Capacity).
    """

    def test_team_effort_hour_capacity_calculation(self):
        """
        Test case to verify the calculation of team effort-hour capacity using TeamEffortHourCalculator class.
        """
        # Scenario: Calculate team effort-hour capacity with multiple team members and varying parameters
        member1 = TeamMember("Anisha", 8, 0, 0)
        member2 = TeamMember("Anshul", 7, 2, 0)
        member3 = TeamMember("Anjali", 6, 0, 3)
        member4 = TeamMember("Arnav", 8, 1, 2)

        # Create TeamEffortHourCalculator object
        calculator = TeamEffortHourCalculator()

        # Add team members to the calculator
        calculator.add_team_member(member1)
        calculator.add_team_member(member2)
        calculator.add_team_member(member3)
        calculator.add_team_member(member4)

        # Exercise the feature (happy path)
        total_effort_hours = calculator.calculate_total_effort_hours(10)

        # Verify the result
        self.assertEqual(total_effort_hours, 234)
        print("Acceptance test (happy path) passed: Total effort-hours for the team is 234")

        # Additional test: Verify adding team members (additional method exercise)
        self.assertEqual(len(calculator.team_members), 4)
        print("Acceptance test (additional method) passed: Team members added successfully")

        # Scenario: Calculate team effort-hour capacity with no team members (unhappy path)
        calculator_no_members = TeamEffortHourCalculator()

        # Exercise the feature (unhappy path)
        total_effort_hours_no_members = calculator_no_members.calculate_total_effort_hours(10)

        # Verify the result
        self.assertEqual(total_effort_hours_no_members, 0)
        print("Acceptance test (unhappy path) passed: Total effort-hours for the team is 0 (no team members)")

if __name__ == '__main__':
    unittest.main()
