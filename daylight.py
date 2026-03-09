def calculate_sleep_debt(planned, actual):
  # Write code below 💖
  """
  Tracking sleep debt
  Args:
  planned (list): intended hours to sleep
  actual (list): actually sleep hours
  Returns:
  total sleep debt for the week (including +1 Daylight Savings hour)
  longest streak of consecutive days with sleep debt
  """
  debt = [planned[i] - actual[i] for i in range(len(planned))]
  sleep_debt = [0 if num < 0 else num for num in debt]
  time_diff = list()
  for el in range(1, len(sleep_debt)):
    if sleep_debt[el] != 0:
      delta = abs(sleep_debt[el-1] * sleep_debt[el])
      if delta != 0:
        d = abs(sleep_debt[el-1] - sleep_debt[el])
        time_diff.append(d)
    else:
      continue
  return sum(sleep_debt)+1, len(time_diff)+1

# example
print(calculate_sleep_debt([7.5, 8, 7.5, 8, 8.5, 8, 7.5], [5, 12, 6, 6, 9, 8, 6.5]))
