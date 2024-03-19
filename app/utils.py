from datetime import timedelta

def calculate_time_taken(test_result):
  """
  Calculates the time taken for the test and formats it as 'Xm Ys' (minutes and seconds).

  Args:
      test_result: A dictionary containing test start and end time information.

  Returns:
      A string representing the time taken in 'Xm Ys' format (e.g., '59m 46s').
  """

  time_delta = test_result.end_time - test_result.start_time  # Calculate time difference

  # Extract minutes and seconds (ignore days and hours as requested)
  minutes = time_delta.seconds // 60
  seconds = time_delta.seconds % 60

  # Format the time taken string
  time_taken_str = f"{minutes}m {seconds}s"

  return time_taken_str