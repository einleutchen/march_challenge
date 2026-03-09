def find_missing_colors(grid):
  # Write code below 💖
  """
  Find the emojis that are missing from a given array of emojis
  Args:
  grid (list of list): arrays of emojis
  Returns:
  the missing emojis in order
  """
  given_array = ["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "🟫"]
  diff_list = []
  for i in grid:
    to_set = set(i)
    given_set = set(given_array)
  if given_set & to_set:
    diff_list.extend(sorted(list(given_set - to_set)))
    return diff_list
  else:
    return given_array

test = [["🟥", "🟧", "🟨", "🟩", "🟦", "🟥", "🟧"],     
["🟨", "🟩", "🟦", "🟥", "🟨", "🟩", "🟦"],     
["🟥", "🟧", "🟨", "🟩", "🟦", "🟥", "🟨"],     
["🟩", "🟦", "🟥", "🟧", "🟨", "🟩", "🟦"],     
["🟨", "🟥", "🟧", "🟨", "🟩", "🟦", "🟥"],     
["🟦", "🟩", "🟨", "🟥", "🟧", "🟩", "🟦"],    
["🟥", "🟧", "🟨", "🟩", "🟦", "🟨", "🟥"]]

print(find_missing_colors(test))
