from datetime import datetime, time, timedelta


def parse_time(value, setting_name):
    """Convert an hour or HH:MM setting to a ``datetime.time`` value."""
    if isinstance(value, time):
        return value

    value = str(value).strip()
    for time_format in ("%H:%M", "%H"):
        try:
            return datetime.strptime(value, time_format).time()
        except ValueError:
            continue

    raise ValueError(
        f"{setting_name} має бути в форматі HH:MM (наприклад, 11:00)"
    )


def calculate_working_minutes(
    start_dt,
    end_dt,
    work_start,
    work_end,
    lunch_start,
    lunch_end,
):
    if start_dt >= end_dt:
        return 1

    total_minutes = 0
    current_day = start_dt.date()

    while current_day <= end_dt.date():
        work_start_dt = datetime.combine(current_day, work_start)
        work_end_dt = datetime.combine(current_day, work_end)
        actual_start = max(start_dt.replace(tzinfo=None), work_start_dt)
        actual_end = min(end_dt.replace(tzinfo=None), work_end_dt)

        if actual_start < actual_end:
            total_minutes += (actual_end - actual_start).total_seconds() / 60

            lunch_start_dt = datetime.combine(current_day, lunch_start)
            lunch_end_dt = datetime.combine(current_day, lunch_end)
            overlap_start = max(actual_start, lunch_start_dt)
            overlap_end = min(actual_end, lunch_end_dt)

            if overlap_start < overlap_end:
                total_minutes -= (
                    overlap_end - overlap_start
                ).total_seconds() / 60

        current_day += timedelta(days=1)

    return max(1, round(total_minutes))
