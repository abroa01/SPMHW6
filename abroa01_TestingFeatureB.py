import unittest
from SprintVelocity import TeamMember, TeamEffortHourCalculator

class unitTest_TestTeamMember(unittest.TestCase):

    def test_calculate_effort_hours(self):
        # Create a team member with various attributes
        member = TeamMember("John", 8, 1, 1)  # 8 hours/day, 1 vacation day, 1 ceremony day

        # Test case 1: All parameters within expected range
        expected_hours = 8 * (10 - 1 - 1)
        actual_hours = member.calculate_effort_hours(10)
        self.assertEqual(actual_hours, expected_hours)
        print("Test case 1 passed: Expected hours =", expected_hours, ", Actual hours =", actual_hours)

        # Test case 2: Zero vacation days
        member.vacation_days = 0
        expected_hours = 8 * (10 - 0 - 1)
        actual_hours = member.calculate_effort_hours(10)
        self.assertEqual(actual_hours, expected_hours)
        print("Test case 2 passed: Expected hours =", expected_hours, ", Actual hours =", actual_hours)

        # Test case 3: Zero ceremony days
        member.ceremony_days = 0
        expected_hours = 8 * (10 - 0 - 0)
        actual_hours = member.calculate_effort_hours(10)
        self.assertEqual(actual_hours, expected_hours)
        print("Test case 3 passed: Expected hours =", expected_hours, ", Actual hours =", actual_hours)

        # Test case 4: Zero vacation days and zero ceremony days
        member.vacation_days = 0
        expected_hours = 8 * (10 - 0 - 0)
        actual_hours = member.calculate_effort_hours(10)
        self.assertEqual(actual_hours, expected_hours)
        print("Test case 4 passed: Expected hours =", expected_hours, ", Actual hours =", actual_hours)

        # Test case 5: Zero sprint days
        expected_hours = 0
        actual_hours = member.calculate_effort_hours(0)
        self.assertEqual(actual_hours, expected_hours)
        print("Test case 5 passed: Expected hours =", expected_hours, ", Actual hours =", actual_hours)

        # Test case 6: Negative sprint days (should return 0)
        expected_hours = 0
        actual_hours = member.calculate_effort_hours(-5)
        self.assertEqual(actual_hours, expected_hours)
        print("Test case 6 passed: Expected hours =", expected_hours, ", Actual hours =", actual_hours)

        # Test case 7: Negative hours per day (should return 0)
        member.hours_per_day = -8
        expected_hours = 0
        actual_hours = member.calculate_effort_hours(10)
        self.assertEqual(actual_hours, expected_hours)
        print("Test case 7 passed: Expected hours =", expected_hours, ", Actual hours =", actual_hours)

class acceptanceTest_TestFeatureB(unittest.TestCase):

    def test_calculate_total_effort_hours_happy_path(self):
        # Test case 1: Calculate total effort-hours for a 10-day sprint with no vacation days and ceremony days
        member1 = TeamMember("John", 8, 0, 0)  # 8 hours/day, no vacation days, no ceremony days
        member2 = TeamMember("Jane", 7, 0, 0)  # 7 hours/day, no vacation days, no ceremony days
        calculator = TeamEffortHourCalculator()
        calculator.add_team_member(member1)
        calculator.add_team_member(member2)
        total_effort_hours = calculator.calculate_total_effort_hours(10)
        self.assertEqual(total_effort_hours, (8 * 10) + (7 * 10))

    def test_calculate_total_effort_hours_with_vacation_days(self):
        # Test case 2: Calculate total effort-hours for a 10-day sprint with vacation days
        member1 = TeamMember("John", 8, 2, 0)  # 8 hours/day, 2 vacation days, no ceremony days
        member2 = TeamMember("Jane", 7, 3, 0)  # 7 hours/day, 3 vacation days, no ceremony days
        calculator = TeamEffortHourCalculator()
        calculator.add_team_member(member1)
        calculator.add_team_member(member2)
        total_effort_hours = calculator.calculate_total_effort_hours(10)
        self.assertEqual(total_effort_hours, (8 * (10 - 2)) + (7 * (10 - 3)))

    def test_calculate_total_effort_hours_with_ceremony_days(self):
        # Test case 3: Calculate total effort-hours for a 10-day sprint with ceremony days
        member1 = TeamMember("John", 8, 0, 2)  # 8 hours/day, no vacation days, 2 ceremony days
        member2 = TeamMember("Jane", 7, 0, 3)  # 7 hours/day, no vacation days, 3 ceremony days
        calculator = TeamEffortHourCalculator()
        calculator.add_team_member(member1)
        calculator.add_team_member(member2)
        total_effort_hours = calculator.calculate_total_effort_hours(10)
        self.assertEqual(total_effort_hours, (8 * (10 - 2)) + (7 * (10 - 3)))

    def test_calculate_total_effort_hours_zero_sprint_days(self):
        # Test case 4: Calculate total effort-hours for a 0-day sprint
        member1 = TeamMember("John", 8, 1, 1)  # 8 hours/day, 1 vacation day, 1 ceremony day
        member2 = TeamMember("Jane", 7, 2, 1)  # 7 hours/day, 2 vacation days, 1 ceremony day
        calculator = TeamEffortHourCalculator()
        calculator.add_team_member(member1)
        calculator.add_team_member(member2)
        total_effort_hours = calculator.calculate_total_effort_hours(0)
        self.assertEqual(total_effort_hours, 0)

    def test_calculate_total_effort_hours_negative_sprint_days(self):
        # Test case 5: Calculate total effort-hours for a negative number of sprint days (should return 0)
        member1 = TeamMember("John", 8, 1, 1)  # 8 hours/day, 1 vacation day, 1 ceremony day
        member2 = TeamMember("Jane", 7, 2, 1)  # 7 hours/day, 2 vacation days, 1 ceremony day
        calculator = TeamEffortHourCalculator()
        calculator.add_team_member(member1)
        calculator.add_team_member(member2)
        total_effort_hours = calculator.calculate_total_effort_hours(-5)
        self.assertEqual(total_effort_hours, 0)


if __name__ == '__main__':
    unittest.main()
