from datetime import datetime

def expireDate(delay):
    expDate = datetime.datetime.now()
    expDate = expDate + datetime.timedelta(days=delay)
    return expDate