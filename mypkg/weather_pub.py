import requests
from datetime import datetime
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

rclpy.init()
node=Node("weather_pub")
pub=node.create_publisher(String,"weather",10)
n=0


def cb():
    global n
    msg=String()
    msg.data = get_weather()
    pub.publish(msg)


def main():
    node.create_timer(0.5,cb)
    rclpy.spin(node)

def get_weather():
    url=f"https://weather.tsukumijima.net/api/forecast?city=130010"
    response=requests.get(url)
    response.raise_for_status()

    data_json=response.json()

    date_str = data_json["forecasts"][1]["date"]
    date = datetime.strptime(date_str,"%Y-%m-%d").strftime("%Y年%m月%d日")
    title=data_json["title"]
    weather=data_json["forecasts"][1]["telop"]
    max_temp=data_json["forecasts"][1]["temperature"]["max"]["celsius"]
    min_temp=data_json["forecasts"][1]["temperature"]["min"]["celsius"]

    results=f"{date}の{title}は{weather}です。\n最高気温は{max_temp}度、最低気温は{min_temp}度です。"
    return results
