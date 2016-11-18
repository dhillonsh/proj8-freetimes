from agenda import *
#import arrow


def test_noEvents():
  #8AM to 5PM on 1 day
  singleDay = agenda("2016-11-17","2016-11-17","2016-11-17T08:00:00:00", "2016-11-17T17:00:00:00", [])
  assert len(singleDay) == 1
  assert arrow.get(singleDay[0]['start']).format('YYYY-MM-DD HH:mm') == "2016-11-17 08:00"
  assert arrow.get(singleDay[0]['end']).format('YYYY-MM-DD HH:mm') == "2016-11-17 17:00"
  
  #8AM to 5PM over 2 days
  multipleDays = agenda("2016-11-17", "2016-11-18","2016-11-17T08:00:00:00","2016-11-18T17:00:00:00", [])
  assert len(multipleDays) == 2
  assert arrow.get(multipleDays[0]['start']).format('YYYY-MM-DD HH:mm') == "2016-11-17 08:00"
  assert arrow.get(multipleDays[0]['end']).format('YYYY-MM-DD HH:mm') == "2016-11-17 17:00"
  assert arrow.get(multipleDays[1]['start']).format('YYYY-MM-DD HH:mm') == "2016-11-18 08:00"
  assert arrow.get(multipleDays[1]['end']).format('YYYY-MM-DD HH:mm') == "2016-11-18 17:00"

def test_singleEvent():
  busyList = [{'summary': 'randomEvent', 'start': "2016-11-17T08:00:00:00", 'end': "2016-11-17T08:30:00:00"}]
  
  #Event at the start of the day and time
  startDayEvent = agenda("2016-11-17","2016-11-17","2016-11-17T08:00:00:00", "2016-11-17T17:00:00:00", busyList)
  assert len(singleDay) == 2
  #assert arrow.get(singleDay[0]['start']).format('YYYY-MM-DD HH:mm') == "2016-11-17 08:00"
  #assert arrow.get(singleDay[0]['end']).format('YYYY-MM-DD HH:mm') == "2016-11-17 17:00"
  print(startDayEvent)
  #Event at the end of the day and time
  
  #Event in the middle of a day
