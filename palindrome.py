def check_palindrome(sequence):
  # Write code below 💖
  """
  Determines if a sequence is a palindrome.
  Args:
  sequence (str): string of characters
  Returns:
  boolean
  """
  sequence = "".join(sequence.lower().split())
  reversed_sequence = "".join(sequence[::-1].lower().split())
  if sequence == reversed_sequence:
    return True
  else:
    return False

test = "12345"
print(check_palindrome(test))
