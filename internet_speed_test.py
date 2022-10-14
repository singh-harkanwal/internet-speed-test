#This program will test internet speed 
import speedtest

def internetSpeedTest():
    #Create a speed test object
    speed_test = speedtest.Speedtest()
    
    #Find a list of available servers for the internet speed test 
    print("Loading Server List...")
    speed_test.get_servers()
    
    #Choose the best available server
    print("Choosing the best server")
    best_server = speed_test.get_best_server()
    
    #Print the best server host, and its location
    print(f"The best server host is {best_server['host']} located in {best_server['name']}, {best_server['country']}")

    #Print download speed and convert into Mbits/sec
    print(f"Download Speed: {speed_test.download() / 1024 / 1024:.2f} Mbits/sec")
    
    #Print upload speed and convert into Mbits/sec
    print(f"Upload Speed: {speed_test.upload() / 1024 / 1024:.2f} Mbits/sec")
    
    #Print ping result
    print(f"Ping: {speed_test.results.ping:.2f}ms")
    
internetSpeedTest()