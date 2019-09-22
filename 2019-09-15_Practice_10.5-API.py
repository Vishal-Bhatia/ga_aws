#%%
##Creating a simple function for mean & std, for API hosting
# def calc_mean(arr):
#     return sum(arr)/len(arr)

# def calc_std(arr):
#     avg = calc_mean(arr)
#     stdev = 0
#     for elem in arr:
#         stdev += (elem - avg)**2
#     return (stdev/len(arr))**0.5

# std = calc_std([3, 4, 3, 2, 5])
# print(std)

#%%
##Writing code for API hosting
import json
import flask
from flask import Flask, request

app = Flask(__name__)

@app.route("/test", methods = ["GET"])
def test_api():
    return "Success!"

@app.route("/avg", methods = ["POST"])
def calc_mean():
    arr = json.loads(request.data.decode())["arr"]
    print("The input is", arr)
    return str(round(sum(arr)/len(arr), 4))

@app.route("/std", methods = ["POST"])
def calc_std():
    arr = json.loads(request.data.decode())["arr"]
    print("The input is", arr)
    avg = float(calc_mean())
    stdev = 0
    for elem in arr:
        stdev += (elem - avg)**2
    return str(round((stdev/len(arr))**0.5, 4))

if __name__ == "__main__":
    app.run(host = "localhost", port = 5000)


#%%
