import datetime
import time
import re

def QA_util_date_stamp(date):
    #date function
    datestr=str(date)[0:10]
    date=time.mktime(time.strptime(datestr,'%Y-%m-%d'))
    return date
def QA_util_time_stamp(time):
    time=str(time)[0:10]
    
    return time
def QA_util_ms_stamp(ms):
    return ms

def QA_util_date_valid(date):
    try:
        
        time.strptime(date, "%Y-%m-%d")
        return True
    except:
        return False
def QA_util_realtime(strtime,client):
    time_stamp=QA_util_date_stamp(strtime)
    coll=client.quantaxis.trade_date
    temp_str=coll.find_one({'date_stamp':{"$gte":time_stamp}})
    time_real=temp_str['date']
    time_id=temp_str['num']
    return {'time_real':time_real,'id':time_id}