import unittest
from datetime import datetime, time

from working_hours import calculate_working_minutes, parse_time


class WorkingHoursTest(unittest.TestCase):
    def test_parse_time_accepts_hour_and_hour_minute(self):
        self.assertEqual(parse_time(11, "WORK_START"), time(11, 0))
        self.assertEqual(parse_time("11:30", "WORK_START"), time(11, 30))

    def test_minutes_before_configured_start_are_not_counted(self):
        minutes = calculate_working_minutes(
            datetime(2026, 9, 22, 10, 0),
            datetime(2026, 9, 22, 12, 0),
            time(11, 0), time(19, 0), time(14, 0), time(15, 0),
        )
        self.assertEqual(minutes, 60)

    def test_deal_created_before_work_starts_counts_from_work_start(self):
        minutes = calculate_working_minutes(
            datetime(2026, 9, 22, 9, 59),
            datetime(2026, 9, 22, 11, 20),
            time(11, 0), time(19, 0), time(14, 0), time(15, 0),
        )
        self.assertEqual(minutes, 20)

    def test_lunch_is_excluded(self):
        minutes = calculate_working_minutes(
            datetime(2026, 9, 22, 13, 0),
            datetime(2026, 9, 22, 16, 0),
            time(11, 0), time(19, 0), time(14, 0), time(15, 0),
        )
        self.assertEqual(minutes, 120)


if __name__ == "__main__":
    unittest.main()
