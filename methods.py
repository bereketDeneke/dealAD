import datetime

def expireDate(delay):
    expDate = datetime.datetime.now()
    expDate = expDate + datetime.timedelta(days=delay)
    print("================================")
    print(expDate)
    print("================================")
    return expDate