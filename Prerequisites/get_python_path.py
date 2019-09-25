import requests

## Change of the path retrieval part
from distutils import sysconfig

bindir = sysconfig.get_config_vars("BINDIR")

def convert(bindir):
    a=''
    for i in bindir:
        a = a+i
        return a

pythonPath = convert(bindir)
with open("../config.csv", "w") as f:
    f.write("PythonPath,{}\nCheckWindowsCredentials,true".format(pythonPath))
    print("=== Python Path written to config file.===")

## Change of the path retrieval part

print("Downloading ML model... Please don't close this window.")

url = "https://github.com/andumorie/uipath-face-recognition-framework/raw/master/FaceRecognition/model/20170511-185253.pb"
r = requests.get(url)

with open('../FaceRecognition/model/20170511-185253.pb', 'wb') as f:  
    f.write(r.content)

if r.status_code == 200:
    print("Download completed successfully!")
else:
    print("An error occured while downloading the model. Please check your internet connection and try again.")
