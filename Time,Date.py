from flask import *
import datetime
import pytz

time_help = '''
===Time Commands===;
#TimeZone display#
Ex***- APIURL/time/get/[pick below on which timezone to put here] *note put the timezone without the []
sl = Sri Lanka/Colombo Time
eusa = Eastern USA 
aus = Australia/Brisbane
lon = England/London
'''
date_help = '''
None Yet...
'''

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def main():
   print('Connected')
   return 'connected'

'''Time Section'''
@app.route('/time/help', methods = ['GET'])
def time_help():
    print(time_help)
    return time_help

@app.route('/time/get/<tizo>', methods = ['GET'])
def time(tizo):
    now = datetime.now()
    if tizo == 'sl':
        tz = pytz.timezone('Asia/Colombo')
    elif tizo == 'eusa':
        tz = pytz.timezone('US/Eastern')
    elif tizo == 'aus':
        tz = pytz.timezone('Australia/Brisbane')
    elif tizo == 'lon':
        tz = pytz.timezone('Europe/London')
    now_tz = now.astimezone(tz)
    print(now_tz)
    now_tz = str(now_tz)
    return now_tz

'''Date Section'''
@app.route('/date/help', methods = ['GET'])
def date_help():
    print(date_help)
    return date_help

if __name__ == "__main__":
    print('Server on')
    app.run('0.0.0.0', 2046, False)
    print('server off')