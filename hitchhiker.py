def minimum_components(components):
  # Write code below 💖
  """
  Find the minimum number of components whose sum is exactly 42
  Args:
  components (list): array of integers
  Returns:
  an number (int) of components summed up to 42
  """
  amount = 42
  components.sort()
  dp = [0] * (amount + 1) 
  if sum(components) < amount:
    return -1
  else:
    for i in range(1, amount + 1):
      minn = float("inf")
      for num in components:
        diff = i - num
        if diff < 0: 
          break
        minn = min(minn, dp[diff] + 1)
      dp[i] = minn
    
    if dp[amount] < float("inf"):
      return dp[amount]
    else:
      return -1

components = [43, 45, 41, 1]
print(minimum_components(components))


        
            
