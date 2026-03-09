def analyze(percentages):
  # Write code below 💖
  """
  Return the net change, trend and dips in percentage of women in tech companies
  Args:
  percentages (list): percentage of women in each year
  Returns:
  net change, trend, dips
  """
  net_change = round((percentages[-1] - percentages[0])/(len(percentages)-1), 4)
  average = sum(percentages)/len(percentages)
  trianno = sum(percentages[-4:-1])/3
  trend = "improving" if trianno > average else "stagnating" if trianno == average else "declining"
  diff = [percentages[i] - percentages[i-1] for i in range(1, len(percentages))]
  dips = [num for num in diff if num < 0]
  return net_change, trend, len(dips)

test = [42.0, 43.0, 42.0, 43.0, 44.0, 44.0, 44.6, 44.8, 44.7, 45.0, 45.8]
print(analyze(test))
