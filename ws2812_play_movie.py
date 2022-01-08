import cv2
import time
import sys

from rpi_ws281x import Color, PixelStrip, ws

WIDTH = 54
HEIGHT = 17

# LED strip configuration:
LED_COUNT = WIDTH * HEIGHT   # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0
#LED_STRIP = ws.SK6812_STRIP_RGBW
LED_STRIP = ws.SK6812W_STRIP


if __name__ == '__main__':
    # Create PixelStrip object with appropriate configuration.
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    vidcap = cv2.VideoCapture(sys.argv[1])

    framespersecond = int(vidcap.get(cv2.CAP_PROP_FPS))

    while True:
        success,image = vidcap.read()
        if not success:
            break

        STEP = 1

        dim = (WIDTH, HEIGHT * STEP)

        # resize image
        resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

        for pixel in range(WIDTH * HEIGHT):
            x = HEIGHT - pixel // WIDTH - 1
            y = WIDTH - pixel % WIDTH - 1

            if x % 2 == 0:
                y = WIDTH - y - 1
            white = min(resized[x*STEP][y])
            color = Color(int(resized[x*STEP][y][2]-white), int(resized[x*STEP][y][1]-white), int(resized[x*STEP][y][0]-white), int(white))
            strip.setPixelColor(pixel, color)

        strip.show()
        #time.sleep(1/framespersecond)
