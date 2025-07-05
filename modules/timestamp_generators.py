import time
from datetime import datetime

def reddit_timestamp_creator(unix_epoch):
    # Convert to local datetime object
    dt = datetime.fromtimestamp(unix_epoch)

    # Extract components
    month = dt.month
    day = dt.day
    year = dt.year
    hour = dt.hour
    minute = dt.minute

    am_pm = "am" if hour < 12 else "pm"
    hour_12 = hour % 12 or 12

    return f"{month}/{day}/{year} at {hour_12}:{minute:02d} {am_pm}"

def reddit_account_age_timestamp_generator(unix_epoch):
    return time.strftime("%B %d, %Y", time.localtime(unix_epoch))