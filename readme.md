# Logging data from V5 Brain in Redis

## Getting started
1. Download the main.py file to your robot. If you are using the VSCode extension, click the download button on the blue bar at the bottom.
2. Install dependency's on your local machine
   * If you don't already have python you need to install it.
     * Windows: Go to [Python's website](https://www.python.org/downloads/). Any version should work.
     * MacOS/Linux: You should already have Python installed.
   * Install redis python package
     * Open command prompt or terminal and run the following:
   * You also need to have Redis with the Time Series module installed. [Check out this guide](https://redis.io/docs/stack/timeseries/quickstart/)
     ``` bash
     python -m pip install redis
     ```
3. Start the program on the robot
4. Run decode.py
   * If you have it open in VSCode click on the run arrow in the top right.
   * You might be able to double click on it, or start it from the command line/terminal:
     ``` bash
     python decode.py
     ```
5. Select the serial port.
   * Windows: Check device manager then select the correct COM port
   * MacOS: It is normally `cu.usbmodem-113` (Note: I need to double check)

You should now be logging data in Redis. [You might also want to install Grafana](https://grafana.com/docs/grafana/latest/setup-grafana/installation/)