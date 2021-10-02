import time as t
import pyautogui as pg

def main():
    """Values that you might want to change"""
    ScreenResolutionWidth = 1920
    ScreenResolutionHeight = 1080

    """Values that you will want to change"""
    "Time until you join the queue:"
    Hours = 4
    Minutes = 30

    """Values you should not touch"""
    WidthScaling = 1678/1920
    HeightScaling = 957/1080
    xPixel = ScreenResolutionWidth*WidthScaling
    yPixel = ScreenResolutionHeight*HeightScaling
    sleepTime = Hours*3600 + Minutes*60

    """Logic you should not touch"""
    for i in range(3):
        pg.moveTo(ScreenResolutionWidth/2, ScreenResolutionHeight/2)
    t.sleep(1)
    print("Starting autoqueue: please navigate to the screen in New World where you join the queue")
    print("Joining queue in " + str(Hours) + " hours and " + str(Minutes) + " minutes.")
    t.sleep(sleepTime)
    for i in range(3):
        pg.moveTo(ScreenResolutionWidth/2, ScreenResolutionHeight/2)
        pg.click()
    t.sleep(1)
    for i in range(3):
        t.sleep(1)
        pg.moveTo(xPixel, yPixel)
        pg.click()
    t.sleep(1)
    for i in range(3):
        pg.moveTo(ScreenResolutionWidth - 20, ScreenResolutionHeight - 20)
        pg.click()

if __name__ == "__main__":
    main()
