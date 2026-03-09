def time_cal(distance, rate):
  """
  Calculate the time to finish a distance (km) with a given speed (km/s)
  Args:
  distance (list): start and end points
  rate (int): velocity value
  Returns:
  time in seconds
  """
  diff = (distance[-1] - distance[0])
  time = diff/rate
  return time

def calculate_descent(altitude):
  # Write code below 💖
  """
  Calculate the total descent time from a given altitude till the ground
  Args:
  altitude (int): number not exceeding 10000km
  Returns:
  total time in seconds
  """
  exosphere = time_cal([700,10000], 2)
  thermosphere = time_cal([85, 700], 0.5)
  mesosphere = time_cal([50, 85], 0.2)
  stratosphere = time_cal([12, 50], 0.075)
  troposphere = time_cal([0, 12], 0.02)
  atm = [exosphere, thermosphere, mesosphere, stratosphere, troposphere]
  
  if altitude > 700:
    total_time = round(time_cal([700, altitude], 2) + sum(atm[1:]),1)
  elif 85 < altitude and altitude < 700:
    total_time = round(time_cal([85, altitude], 0.5) + sum(atm[2:]),1)
  elif 50 < altitude and altitude < 85:
    total_time = round(time_cal([50, altitude], 0.2) + sum(atm[3:]),1)
  elif 12 < altitude and altitude < 50:
    total_time = round(time_cal([12, altitude], 0.075) + sum(atm[4:]),1)
  else:
    total_time = round(time_cal([0, altitude], 0.02) + sum(atm[5:]),1)
 
  return(total_time)

calculate_descent(200)
