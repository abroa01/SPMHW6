import unittest
from SprintVelocity import Sprint, SprintManager

class TestSprintManager(unittest.TestCase):
    """
    Test case class for testing the SprintManager class.
    """

    def test_calculate_average_velocity(self):
        """
        Test case to verify the calculate_average_velocity method of the SprintManager class.
        """
        print("Running test_calculate_average_velocity...")
        sprint_manager = SprintManager()

        # Test case: No sprints
        print("Test case: No sprints")
        self.assertEqual(sprint_manager.calculate_average_velocity(), 0)
        print("Test case passed: Average velocity is 0")

        # Test case: Sprints with zero total points
        print("Test case: Sprints with zero total points")
        sprint1 = Sprint(1, "2024-03-01", "2024-03-14")
        sprint2 = Sprint(2, "2024-03-15", "2024-03-28")
        sprint_manager.accept_sprints_list([sprint1, sprint2])
        self.assertEqual(sprint_manager.calculate_average_velocity(), 0)
        print("Test case passed: Average velocity is 0")

        # Test case: Sprints with varying total points
        print("Test case: Sprints with varying total points")
        sprint1.total_points = 10
        sprint2.total_points = 20
        self.assertEqual(sprint_manager.calculate_average_velocity(), 15)
        print("Test case passed: Average velocity is 15")

        # Test case: One sprint with total points
        print("Test case: One sprint with total points")
        sprint_manager.accept_sprints_list([sprint1])
        self.assertEqual(sprint_manager.calculate_average_velocity(), 10)
        print("Test case passed: Average velocity is 10")

if __name__ == '__main__':
    unittest.main()
