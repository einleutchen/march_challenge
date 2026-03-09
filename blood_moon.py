def blood_moon(time):
  # Write code below 💖
  """
  Return the blood moon times for the next 3 blood moons after the given time.
  Args:
    time (str): The starting time in "HH:MM" format.
  Returns:
    list: A list of the next 3 blood moon times in "HH:MM" format.
  """
  current_time = time.split(":")
  hour = int(current_time[0])
  minute = int(current_time[-1])
  hour_list = [hour]
  minute_list = [minute]
  time_list = list()

  if hour + 2 < 24:
    for i in range(3):
      h = hour_list[-1] + 2 
      m = minute_list[-1] + 48
      hour_list.append(h)
      minute_list.append(m)
      if m > 60:
        print("min > 60")
        new_h = h + int(m/60)
        new_m = m - int(m/60) * 60
        txt1 = "{:02d}:{:02d}".format(new_h, new_m)
        time_list.append(txt1)
      else:
        txt2 = "{:02d}:{:02d}".format(h, m)
        time_list.append(txt2)

  else:
    for i in range(3):
      h = hour_list[-1] + 2
      if h >= 24:
        h = h - 24
        hour_list.append(h)
      else:
        hour_list.append(h) 
      m = minute_list[-1] + 48
      minute_list.append(m)
      if m > 60:
        print("min > 60")
        new_h = h + int(m/60)
        new_m = m - int(m/60) * 60
        txt1 = "{:02d}:{:02d}".format(new_h, new_m)
        time_list.append(txt1)
      else:
        txt2 = "{:02d}:{:02d}".format(h, m)
        time_list.append(txt2)
  
  return time_list

bloodmoon = blood_moon("23:50")
print(bloodmoon)