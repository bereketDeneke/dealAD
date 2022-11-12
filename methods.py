import datetime

def expireDate(delay):
    expDate = datetime.datetime.now()
    expDate = expDate + datetime.timedelta(days=delay)
    epoch = datetime.datetime.utcfromtimestamp(0)
    timeStamp =  (expDate - epoch).total_seconds()
    # total_seconds will be in decimals (millisecond precision)
    return timeStamp