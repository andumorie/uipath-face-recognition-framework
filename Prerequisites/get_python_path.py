import sys

for path in sys.path:
    if path.endswith("Python36") or path.endswith("Python36\\"):
        with open("../config.csv", "w") as f:
            f.write("PythonPath,{}".format(path))
            print("Python Path written to config file.")
            break