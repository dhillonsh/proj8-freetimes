import arrow

def agenda(startDay, endDay, startTime, endTime, busyList):
  begin_time = arrow.get(startTime)
  end_time = arrow.get(endTime)
  begin_date = arrow.get(startDay).replace(hour=begin_time.hour, minute=begin_time.minute)
  end_date = arrow.get(endDay).replace(hour=end_time.hour, minute=end_time.minute)

  cur_time = begin_date
  fullAgenda = []
  for event in busyList:
    event_start = arrow.get(event['start'])
    event_end = arrow.get(event['end'])
    
    if cur_time < event_start:
      while cur_time < event_start.replace(hour=begin_time.hour,minute=begin_time.minute):
        if cur_time < cur_time.replace(hour=end_time.hour, minute=end_time.minute):
          toAppend = {'summary': 'Available', 'start': cur_time.format("ddd MM/DD/YYYY HH:mm"), 'end': cur_time.replace(hour=end_time.hour, minute=end_time.minute).format("ddd MM/DD/YYYY HH:mm")}
          toAppend['formattedDate'] = formatDates(toAppend['start'], toAppend['end'])
          fullAgenda.append(toAppend)
        cur_time = cur_time.replace(hour=begin_time.hour, minute=begin_time.minute,days=+1)
      toAppend = {'summary': 'Available', 'start': cur_time.format("ddd MM/DD/YYYY HH:mm"), 'end': event_start.format("ddd MM/DD/YYYY HH:mm")}
      toAppend['formattedDate'] = formatDates(toAppend['start'], toAppend['end'])
      fullAgenda.append(toAppend)
    cur_time = event_end
    fullAgenda.append(event)

  #Fill in the days after the last event as available
  while cur_time < end_date:
    if cur_time < cur_time.replace(hour=end_time.hour, minute=end_time.minute):
      toAppend = {'summary': 'Available', 'start': cur_time.format("ddd MM/DD/YYYY HH:mm"), 'end': cur_time.replace(hour=end_time.hour, minute=end_time.minute).format("ddd MM/DD/YYYY HH:mm")}
      toAppend = formatDates(toAppend['start'], toAppend['end'])
      fullAgenda.append(toAppend)
    cur_time = cur_time.replace(hour=begin_time.hour, minute=begin_time.minute,days=+1)
  return fullAgenda

def formatDates(startDate, endDate):
  timeFormats = ["ddd MM/DD/YYYY HH:mm", "YYYY-MM-DD HH:mm:ssZZ"]
  print(startDate)
  startOBJ = arrow.get(startDate, timeFormats)
  print("Here")
  endOBJ = arrow.get(endDate, "ddd MM/DD/YYYY HH:mm")
  if startOBJ.format("ddd MM/DD/YYYY") == endOBJ.format("ddd MM/DD/YYYY"):
    return startOBJ.format("ddd MM/DD/YYYY") + ": " + startOBJ.format("HH:mm") + " - " + endOBJ.format("HH:mm")
  return startOBJ.format("ddd MM/DD/YYYY HH:mm") + ' - ' + endOBJ.format("ddd MM/DD/YYYY HH:mm")   
