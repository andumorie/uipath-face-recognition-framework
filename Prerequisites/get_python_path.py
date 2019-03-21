import requests
import sys

for path in sys.path:
    if path.endswith("Python36") or path.endswith("Python36\\"):
        with open("../config.csv", "w") as f:
            f.write("PythonPath,{}".format(path))
            print("Python Path written to config file.")
            break


print("Downloading ML model... Please don't close this window.")

url = "https://github.com/andumorie/uipath-face-recognition-framework/raw/master/FaceRecognition/model/20170511-185253.pb"
r = requests.get(url)

with open('../FaceRecognition/model/20170511-185253.pb', 'wb') as f:  
    f.write(r.content)

if r.status_code == 200:
    print("Download completed successfully!")
else:
    print("An error occured while downloading the model. Please check your internet connection and try again.")
