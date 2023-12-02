import requests
import xml.etree.ElementTree as elemtree

def dochak():
    key = 'C5Y9dvMQW/IOpGodBlG0LeFQ9//a6QHsuugGpy11Cj9OhPEF5e+bNibPWcSfSAuS09XgQ7kK2X/bE7BNxN4XdQ=='

    route_str = {"207000016": "1", "207000097": "12", "207000026": "133", "207000033": "23", "207000019": "3", "229000032": "34", 
                "207000103": "360", "207000034": "5", "229000062": "38", "241005970": "7200", "241005960": "7300"}

    d_url = 'http://apis.data.go.kr/6410000/busarrivalservice/getBusArrivalList'
    d_params ={'serviceKey' : key, 'stationId' : '207000273'}

    d_response = requests.get(d_url, params=d_params).text
    d_tree = elemtree.fromstring(d_response)

    msgBody = d_tree.find('./msgBody')
    xml_bus_list = msgBody.findall('./busArrivalList')

    name_list = []
    low_list = []
    time_list = []
    station_list = []

    for i in xml_bus_list:
        name = i.find('./routeId').text
        name_list.append(route_str[name])
        low = i.find('./lowPlate1').text
        low_list.append(low)
        time = i.find('./predictTime1').text
        time_list.append(time)
        station = i.find('./locationNo1').text
        station_list.append(station)

    return name_list, low_list, time_list, station_list