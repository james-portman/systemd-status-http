import sys
import subprocess
from flask import Flask

app = Flask(__name__)

SERVICE_NAME = sys.argv[1]

@app.route("/")
def root():
    status = check()
    if status:
        http_code = 200
    else:
        http_code = 500
    return str(status), http_code

def check():
    cmd = '/bin/systemctl status %s' % SERVICE_NAME
    proc = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE)
    stdout_list = proc.communicate()[0].split('\n')
    for line in stdout_list:
        if 'Active:' in line:
            if '(running)' in line:
                return True
    return False

app.run(host="0.0.0.0", port=5000)
