import board
import neopixel
import json


from flask import Flask, jsonify, request
app = Flask(__name__)
# app.run(host='0.0.0.0', port=5000, debug=True)

pixel_pin = board.D18
 
# The number of NeoPixels
num_pixels = 12
 
# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRBW
 
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1.0, auto_write=True,
                           pixel_order=ORDER)
pixels.fill((0,0,0,0))

@app.route("/")
def lights():
    all_args = request.args
    print(all_args)

    data = json.loads(all_args.get('lights'))
    print(data)
    
    light = 0
    for index, val in enumerate(data) :
        print(index,val)
        pixels[index] = (val[0],val[1],val[2],val[3])
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
