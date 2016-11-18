from agenda import *
#import arrow


def test_noEvents():
  singleDay = agenda("2016-11-17","2016-11-17","2016-11-17T08:00:00:00", "2016-11-17T17:00:00:00", [])
  assert len(singleDay) == 1
  assert singleDay[0]['start'].format('YYYY-MM-DD HH:mm') == "2016-11-17 08:00"
  assert singleDay[0]['end'].format('YYYY-MM-DD HH:MM') == "2016-11-17 17:00"
  
  multipleDays = agenda("2016-11-17", "2016-11-18","2016-11-17T08:00:00:00","2016-11-18T17:00:00:00", [])
  assert len(multipleDays) == 2
  print(multipleDays)
