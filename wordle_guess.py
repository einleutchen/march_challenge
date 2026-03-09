def wordle_guess(secret : str, guess : str):
  # Write code below 💖
  """
  Returns the number of matches between secret message and guess

  Args:
  secret (str): secret message 
  guess (str): guess characters

  Returns:
  number of matches (int)
  """
  try:
    match = 0
    secret = secret.lower()
    guess = guess.lower()
    for element in enumerate(guess):
      if element in enumerate(secret): 
        match += 1
    return match
  except (TypeError, AttributeError) as error:
    print("must be string")
    print(erorr)

print(wordle_guess(secret, guess))
