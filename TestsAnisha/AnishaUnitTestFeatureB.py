import unittest
from SprintVelocity import TeamMember

class TestTeamMember(unittest.TestCase):
    def test_calculate_effort_hours(self):
        # Test case: No vacation days, no ceremony days
        member1 = TeamMember("Anisha", 8, 0, 0)
        expected_hours1 = 80
        actual_hours1 = member1.calculate_effort_hours(10)
        self.assertEqual(actual_hours1, expected_hours1)
        print(f"Test case 1 passed: {member1.name} - Expected: {expected_hours1} hours, Actual: {actual_hours1} hours")

        # Test case: Vacation days, no ceremony days
        member2 = TeamMember("Anshul", 7, 2, 0)
        expected_hours2 = 56
        actual_hours2 = member2.calculate_effort_hours(10)
        self.assertEqual(actual_hours2, expected_hours2)
        print(f"Test case 2 passed: {member2.name} - Expected: {expected_hours2} hours, Actual: {actual_hours2} hours")

        # Test case: No vacation days, ceremony days
        member3 = TeamMember("Anjali", 6, 0, 3)
        expected_hours3 = 42
        actual_hours3 = member3.calculate_effort_hours(10)
        self.assertEqual(actual_hours3, expected_hours3)
        print(f"Test case 3 passed: {member3.name} - Expected: {expected_hours3} hours, Actual: {actual_hours3} hours")

        # Test case: Vacation days and ceremony days
        member4 = TeamMember("Arnav", 8, 1, 2)
        expected_hours4 = 56
        actual_hours4 = member4.calculate_effort_hours(10)
        self.assertEqual(actual_hours4, expected_hours4)
        print(f"Test case 4 passed: {member4.name} - Expected: {expected_hours4} hours, Actual: {actual_hours4} hours")

if __name__ == '__main__':
    unittest.main()
