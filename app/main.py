class OnlineCourse:

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        """
        Convert days to weeks.

        Args:
            days (int): The number of days.

        Returns:
            int: The number of weeks (round up for any extra days).
        """
        return (days + 6) // 7  # Round up to the next week if there are extra days.

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        """
        Create an instance of OnlineCourse from a dictionary.

        Args:
            cls: The class itself.
            course_dict (dict): A dictionary with course data.

        Returns:
            OnlineCourse: A new instance of the class.
        """
        weeks = cls.days_to_weeks(course_dict["days"])
        return cls(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=weeks
        )
