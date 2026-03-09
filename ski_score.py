def calculate_score(elements):
  # Write code below 💖
  score = []
  for tup in elements:
    GOE = list(tup[-1])
    GOE.remove(min(GOE))
    GOE.remove(max(GOE))
    mean_GOE = sum(GOE)/len(GOE)
    base_value = tup[1]
    element_score = base_value + (mean_GOE * 0.1 * base_value)
    score.append(element_score)
  total_score = round(sum(score), 1)
  return total_score

elements = [
  ("Triple Flip",            9.7,  [3, 2, 3, 3, 2, 4, 3, 2, 3]),
  ("Triple Lutz+Toe Combo", 12.5,  [4, 5, 4, 5, 5, 4, 4, 3, 4]),
  ("Triple Salchow",         7.0,  [2, 3, 2, 2, 3, 2, 2, 3, 2]),
  ("Triple Loop",            6.0,  [3, 3, 2, 4, 3, 3, 2, 3, 2]),
  ("Step Sequence",          3.3,  [4, 4, 4, 4, 3, 3, 4, 3, 4])
]
print(calculate_score(elements))
