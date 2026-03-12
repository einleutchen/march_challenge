def check_url(address):
  # Write code below 💖
  """
  Determine if it's a valid URL or not.
  Args:
  address (str): url as string
  Returns:
  "valid" or "invalid"
  """
  if "https://" in address or "http://" in address:
    domain = address.split(".")
    if len(domain) == 1:
      return "invalid"
    else:
      return "valid"
  else:
      return "invalid"

test = "https://codedex.io"
test2 = "https://www.example.com"

print(check_url(test2))
