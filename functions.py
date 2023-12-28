# returns a string with the current time
def currTime(hour: int, minute: int, am_pm: str):
  out_str = "Current time is: "
  return out_str + timeStr(hour, minute, am_pm)

# returns a string with the wake up time
def wakeupTime(hour: int, minute: int, am_pm: str):
  out_str = "Desired wake up time is: "
  return out_str + timeStr(hour, minute, am_pm)

# calculates the time to wake up after 6 hours
def calcWakeUp(hour: int, minute: int, am_pm: str):
  hour = hour  # temp var
  # convert to 24 hour time
  if (am_pm.upper() == "AM"):
    if (hour == 12):
      hour = 0
  else:
    if (hour != 12):
      hour += 12
  # convert to minutes
  total_minutes = hour * 60 + minute
  # add recommended minimum sleep time (6 hours)
  total_minutes += 60 * 6
  return total_minutes


# prints output for wake up time (6, 7.5, 9 hours of sleep)
def printWakeUp(total_minutes: int):

  out_str = ""
  am_pm = ""
  for i in range(0, 3):
    total_minutes_temp = total_minutes % (60 * 24) + 15
    out_str += "\nYou should wake up at: "
    am_pm = "PM" if (total_minutes_temp / 2) >= 720 else "AM"
    temp = 90 * i
    total_minutes_temp += temp
    out_str += timeStr(total_minutes_temp // 60,
                       total_minutes_temp % 60, am_pm) + " (" + str(6+1.5*i) + " hours)"
  return out_str

def calcSleepTime(hour: int, minute: int, am_pm: str):
  hour = hour  # temp var
  # convert to 24 hour time
  if (am_pm.upper() == "AM"):
    if (hour == 12):
      hour = 0
  else:
    if (hour != 12):
      hour += 12
  # convert to minutes
  total_minutes = hour * 60 + minute
  total_minutes -= 60 * 6
  if (total_minutes < 0):
    total_minutes += 60 * 24
  return total_minutes

def printSleepTime(total_minutes: int):
  out_str = ""
  am_pm = ""
  for i in range (0, 3):
    total_minutes_temp = total_minutes % (60 * 24) - 15
    out_str += "\nYou should go to sleep at: "
    temp = 90 * i
    total_minutes_temp -= temp
    am_pm = "PM" if (total_minutes_temp / 2) >= 720 else "AM"
    out_str += timeStr(total_minutes_temp // 60,
                       total_minutes_temp % 60, am_pm) + " (" + str(6+1.5*i) + " hours)"
  return out_str

def timeStr(hour: int, minute: int, am_pm: str):
  out_str = ""
  if (hour%24 >= 12): # handles case where hours are greater than 12
    am_pm = "PM"
  #hour
  hour_str = str(hour%24%12)
  out_str += hour_str + ":"  # hour
  if (minute < 10):  # minutes
    out_str += "0" + str(minute)
  else:
    out_str += str(minute)
  out_str += " " + am_pm.upper()
  return out_str