import unittest
from datetime import datetime
from SprintVelocity import SprintManager, Sprint

class unitTest_TestSprintManager(unittest.TestCase):

    def test_calculate_total_points_happy_path(self):
        # Happy path scenario where story points are completed for each sprint
        sprint1 = Sprint(1, "2024-03-01", "2024-03-14")
        sprint1.total_points = [5, 8, 3]  # Example story points completed in sprint 1
        sprint2 = Sprint(2, "2024-03-15", "2024-03-28")
        sprint2.total_points = [7, 6, 4]  # Example story points completed in sprint 2

        sprint_manager = SprintManager()
        sprint_manager.accept_sprints_list([sprint1, sprint2])

        sprint_manager.calculate_total_points()

        self.assertEqual(sprint1.total_points, sum([5, 8, 3]), "Total points for sprint 1 incorrect | sprint: 1")
        self.assertEqual(sprint2.total_points, sum([7, 6, 4]), "Total points for sprint 2 incorrect | sprint: 2")

    def test_calculate_total_points_empty_list(self):
        # Unhappy path scenario where the list of sprints is empty
        sprint_manager = SprintManager()
        sprint_manager.accept_sprints_list([])

        sprint_manager.calculate_total_points()

        self.assertEqual(len(sprint_manager.sprints), 0, "No sprints should be present")
        for sprint in sprint_manager.sprints:
            self.assertEqual(sprint.total_points, 0, f"Total points should be 0 for all sprints | sprint: {sprint.sprint_number}")

    def test_calculate_total_points_missing_points(self):
        # Unhappy path scenario where story points are not completed for some sprints
        sprint1 = Sprint(1, "2024-03-01", "2024-03-14")
        sprint1.total_points = [5, 8, 3]  # Example story points completed in sprint 1
        sprint2 = Sprint(2, "2024-03-15", "2024-03-28")
        # No story points completed for sprint 2

        sprint_manager = SprintManager()
        sprint_manager.accept_sprints_list([sprint1, sprint2])

        sprint_manager.calculate_total_points()

        self.assertEqual(sprint1.total_points, sum([5, 8, 3]), "Total points for sprint 1 incorrect | sprint: 1")
        self.assertEqual(sprint2.total_points, 0, "Total points for sprint 2 should be 0 | sprint: 2")


class acceptance_test_TestFeatureA(unittest.TestCase):

    def test_feature_a_happy_path(self):
        # Happy path scenario where story points are completed for each sprint
        sprint1 = Sprint(1, "2024-03-01", "2024-03-14")
        sprint1.total_points = [5, 8, 3]  # Example story points completed in sprint 1
        sprint2 = Sprint(2, "2024-03-15", "2024-03-28")
        sprint2.total_points = [7, 6, 4]  # Example story points completed in sprint 2

        sprint_manager = SprintManager()
        sprint_manager.accept_sprints_list([sprint1, sprint2])

        sprint_manager.calculate_total_points()
        average_velocity = sprint_manager.calculate_average_velocity()

        # Check if the total points for each sprint are correctly calculated
        self.assertEqual(sprint1.total_points, sum([5, 8, 3]), "Total points for sprint 1 incorrect | sprint: 1")
        self.assertEqual(sprint2.total_points, sum([7, 6, 4]), "Total points for sprint 2 incorrect | sprint: 2")

        # Check if the average velocity is correctly calculated and output
        self.assertEqual(average_velocity, (sum([5, 8, 3]) + sum([7, 6, 4])) / 2, "Average velocity incorrect")

    def test_feature_a_empty_sprints(self):
        # Scenario where no sprints are provided
        sprint_manager = SprintManager()
        sprint_manager.accept_sprints_list([])

        sprint_manager.calculate_total_points()
        average_velocity = sprint_manager.calculate_average_velocity()

        # Check if no sprints are present and average velocity is 0
        self.assertEqual(len(sprint_manager.sprints), 0, "No sprints should be present")
        self.assertEqual(average_velocity, 0, "Average velocity should be 0")

    def test_feature_a_missing_points(self):
        # Scenario where story points are not completed for some sprints
        sprint1 = Sprint(1, "2024-03-01", "2024-03-14")
        sprint1.total_points = [5, 8, 3]  # Example story points completed in sprint 1
        sprint2 = Sprint(2, "2024-03-15", "2024-03-28")
        # No story points completed for sprint 2

        sprint_manager = SprintManager()
        sprint_manager.accept_sprints_list([sprint1, sprint2])

        sprint_manager.calculate_total_points()
        average_velocity = sprint_manager.calculate_average_velocity()

        # Check if the total points for each sprint are correctly calculated
        self.assertEqual(sprint1.total_points, sum([5, 8, 3]), "Total points for sprint 1 incorrect | sprint: 1")
        self.assertEqual(sprint2.total_points, 0, "Total points for sprint 2 should be 0 | sprint: 2")

        # Check if the average velocity is correctly calculated and output
        self.assertEqual(average_velocity, sum([5, 8, 3]) / 2, "Average velocity incorrect")


if __name__ == '__main__':
    unittest.main()
