import json
from pathlib import Path

import RPi.GPIO as gpio
import paho.mqtt.subscribe as subscribe
from jinja2 import Template
from sanic import Sanic
from sanic import response

app = Sanic()

pin = 25
gpio.setmode(gpio.BCM)
gpio.setup(pin, gpio.OUT)
is_on = False

index_path = Path(__file__).resolve().parent / 'index.html.jinja'
with open(index_path) as f:
    home_template = Template(f.read())


@app.route("/data")
async def data(request):
    msg = subscribe.simple("garden/sensors")
    return response.json({
        'data': json.loads(msg.payload.decode()),
        'topic': msg.topic
    })


@app.route("/", methods=['POST', 'GET'])
def index(request):
    global is_on
    if request.method == 'POST':
        is_on = not is_on
        gpio.output(pin, is_on)
    return response.html(home_template.render(is_on="on" if is_on else "off"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
