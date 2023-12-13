from gpiozero import LED
import time

led = LED(2)

def main():
  while True:
    print("Turning on LED number 2")
    led.on()
    print("The LED value is %s" % (led.value))
    time.sleep(3)
    print("Turning off LED number 2")
    led.off()
    print("The LED value is %s" % (led.value))
    time.sleep(3)

if __name__ == '__main__':
    main()
