from flask import Flask, render_template
from bus import dochak

app = Flask(__name__)

@app.route('/')
def main():
    name = dochak()[0]
    low = dochak()[1]
    time = dochak()[2]
    station = dochak()[3]
    bus_list = ["1", "12", "133", "23", "3", "34", "360", "38", "5", "7200", "7300"]
    result = find_non_common_elements(name, bus_list)

    b = int(len(name))
    c = int(len(result))

    arrive = []
    arrive_list = []

    for i in range(b):
        if station[i] == "1":
            arrive.append(name[i])
    
    if len(arrive) > 1:
        for i in arrive:
            arrive_list.append(i + "c")

        ar = arrive_list[-1]
        if ar[-1] == "c":
            del(arrive_list[-1])
            arrive_list.append(ar.replace("c", ""))
    else:
        arrive_list = arrive

    return render_template('index.html', name=name, low=low, time=time, station=station, list=list, b=b, range=range, result=result, c=c, arrive_list=arrive_list)

def find_non_common_elements(list1, list2):
    # 두 리스트에서 공통된 문자열을 찾음
    common_elements = set(list1) & set(list2)
    
    # 각 리스트에서 공통된 문자열을 제외한 항목을 찾음
    non_common_elements_list1 = [element for element in list1 if element not in common_elements]
    non_common_elements_list2 = [element for element in list2 if element not in common_elements]
    
    return non_common_elements_list2