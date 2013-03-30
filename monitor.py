import httplib2
import datetime
import time
from random import randint

output_dir = "/var/www/"

def send_request():
    h = httplib2.Http()
    random_number = randint(1000000001,9999999987)
    token_value = ""
    query_url = ""
    before = datetime.datetime.now()
    resp, content = h.request(query_url + str(random_number) + "&", "GET", headers={'TOKEN' : token_value})
    after = datetime.datetime.now()
    diff = after - before
    output = after.strftime('%Y-%m-%d %H:%M') + " response(seconds): " + str(diff.total_seconds()) 

    if int(resp["status"]) == 200:
        status = "OK"
    else:
        status = "ERROR"
    
    file_name = after.strftime('%Y-%m-%d') + "-web_check.log" 
    f = open( output_dir + file_name, "a")	
    log_text = output + " status: " + status + "(" + resp["status"] + ")" + " \n"

    print(log_text)
    f.write(log_text);
    f.close()

    
def check_site():
    while True:
        send_request()
        time.sleep(60)

