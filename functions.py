#utility functions for sweepy.py


# returns a string with the current time
def currTime(hour: int, minute: int, am_pm: str):
  out_str = "Input time is: "
  return out_str + timeStr(hour, minute, am_pm)


# returns a string with the wake up time
def wakeupTime(hour: int, minute: int, am_pm: str):
  out_str = "Desired wake up time is: "
  return out_str + timeStr(hour, minute, am_pm)


# calculates the time to wake up after 6 hours
def calcWakeUp(hour: int, minute: int, am_pm: str):
  hour = hour  # temp var
  # convert to 24 hour time
  if (am_pm.upper() == "AM" and hour == 12):
    hour = 0
  elif (am_pm.upper() == "PM" and hour != 12):
    hour += 12
  # convert to minutes
  total_minutes = hour * 60 + minute
  # add recommended minimum sleep time (6 hours)
  total_minutes += 60 * 6
  return total_minutes


# prints output for wake up time (6, 7.5, 9 hours of sleep)
def printWakeUp(total_minutes: int):
  out_str = ""
  for i in range(0, 3):
    total_minutes_temp = total_minutes % (60 * 24) + 15
    out_str += "\n- You should wake up at: "
    temp = 90 * i
    total_minutes_temp += temp
    out_str += timeTotStr(total_minutes_temp) + " (" + str(6 + 1.5 * i) + " hours)"
  return out_str


def printAllWakeUp(total_minutes: int):
  out_str = ""
  for i in range(1, 8):
    total_minutes_temp = total_minutes % (60 * 24) + 15
    out_str += "\n- You should wake up at: "
    temp = 90 * i
    total_minutes_temp += temp
    out_str += timeTotStr(total_minutes_temp) + " (" + str(1.5 * i) + " hours)"
  return out_str


def calcSleepTime(hour: int, minute: int, am_pm: str):
  hour = hour  # temp var
  # convert to 24 hour time
  if (am_pm.upper() == "AM" and hour == 12):
    hour = 0
  elif (am_pm.upper() == "PM" and hour != 12):
    hour += 12
  # convert to minutes
  total_minutes = hour * 60 + minute
  total_minutes -= 60 * 6
  if (total_minutes < 0):
    total_minutes += 60 * 24
  return total_minutes


def printSleepTime(total_minutes: int):
  out_str = ""
  for i in range(0, 3):
    total_minutes_temp = total_minutes % (60 * 24) - 15
    out_str += "\n- You should go to sleep at: "
    temp = 90 * i
    total_minutes_temp -= temp
    if (total_minutes_temp < 0): # if negative add 720 minutes (am to pm)
      total_minutes_temp += (60 * 24)
    out_str += timeTotStr(total_minutes_temp) + " (" + str(6 + 1.5 * i) + " hours)"
  return out_str


def printAllSleepTime(total_minutes: int):
  out_str = ""
  for i in range(1, 8):
    total_minutes_temp = (total_minutes % (60 * 24)) - 15
    out_str += "\n- You should go to sleep at: "
    temp = 90 * i
    total_minutes_temp -= temp # decrement
    if (total_minutes_temp < 0): # if negative add 720 minutes (am to pm)
      total_minutes_temp += (60 * 24)
    out_str += timeTotStr(total_minutes_temp) + " (" + str(1.5 * i) + " hours)"
  return out_str


def timeStr(hour: int, minute: int, am_pm: str):
  out_str = ""

  hour_str = str(hour) if hour <= 12 else str(hour % 12)

  out_str += hour_str + ":"  # hour
  if (minute < 10):  # minutes
    out_str += "0" + str(minute)
  else:
    out_str += str(minute)
  out_str += " " + am_pm.upper()
  return out_str

def timeTotStr(totalMin: int):
  out_str = ""
  if (totalMin > 60 * 24):
    totalMin = totalMin % (60 * 24)
  hour = totalMin // 60
  minute = totalMin % 60
  am_pm = "PM" if (totalMin >= 720) else "AM"
  if (hour == 0):
    hour = 12
  if (hour > 12):
    hour %= 12
  out_str += str(hour) + ":"  # hour
  if (minute < 10):  # minutes
    out_str += "0" + str(minute)
  else:
    out_str += str(minute)
  out_str += " " + am_pm.upper()
  return out_str
