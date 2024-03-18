from SprintVelocity import Sprint, SprintManager
import unittest

class TestFeatureAAcceptance(unittest.TestCase):
    """
    Acceptance test class for Feature A (Calculate Sprint Velocity).
    """

    def test_sprint_velocity_calculation(self):
        """
        Test case to verify the calculation of sprint velocity using SprintManager class.
        """
        # Scenario: Add sprints with varying total points and calculate average velocity
        sprint1 = Sprint(1, "2024-03-01", "2024-03-14")
        sprint1.total_points = 16
        sprint2 = Sprint(2, "2024-03-15", "2024-03-28")
        sprint2.total_points = 17
        sprint_manager = SprintManager()

        # Add sprints to SprintManager
        sprint_manager.accept_sprints_list([sprint1, sprint2])

        # Exercise the feature (happy path)
        average_velocity = sprint_manager.calculate_average_velocity()

        # Verify the result
        self.assertEqual(average_velocity, 16.5)
        print("Acceptance test (happy path) passed: Average velocity is 16.5")

        # Additional test: Verify adding sprints to SprintManager
        self.assertEqual(len(sprint_manager.sprints), 2)
        print("Acceptance test (additional method) passed: Sprints added successfully")

if __name__ == '__main__':
    unittest.main()
