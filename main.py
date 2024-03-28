import network
import time
import urandom
from umqtt.simple import MQTTClient

# ThingSpeak MQTT broker configuration
mqtt_client_id = "AyoNOS06CjMoFw43NAoZLB4"
mqtt_username = "AyoNOS06CjMoFw43NAoZLB4"
mqtt_password = "LY1GiTeMRed+VV3aM2Wzvh4D"
mqtt_host = "mqtt3.thingspeak.com"
mqtt_port = 1883
topic_temperature = "channels/2488648/publish/fields/field1"
topic_humidity = "channels/2488648/publish/fields/field2"
topic_co2_level = "channels/2488648/publish/fields/field3"

# Wi-Fi connection details
wifi_ssid = "Wokwi-GUEST"
wifi_password = ""

# Store historical sensor data
sensor_data_history = []

# Generates random sensor readings
def generate_random_sensor_values():
    temperature = urandom.uniform(-50, 50) #temperature range in Celsius
    humidity = urandom.uniform(0, 100) #humidity range in %
    co2 = urandom.uniform(300, 2000)  # CO2 levels in ppm
    return temperature, humidity, co2

# Sends sensor data to ThingSpeak
def send_data_to_thingspeak(temperature, humidity, co2_level):
    mqtt_client = MQTTClient(mqtt_client_id, mqtt_host, user=mqtt_username, password=mqtt_password)
    mqtt_client.connect()
    mqtt_client.publish(topic_temperature, str(temperature))
    mqtt_client.publish(topic_humidity, str(humidity))
    mqtt_client.publish(topic_co2_level, str(co2_level))
    mqtt_client.disconnect()

# Establish Wi-Fi connection
network_interface = network.WLAN(network.STA_IF)
network_interface.active(True)
network_interface.connect(wifi_ssid, wifi_password)

# Wait for connection to establish
while not network_interface.isconnected():
    time.sleep(1)  # Wait a bit before re-checking the connection status

print("Wi-Fi Connection Established")

# Main loop to periodically generate and send sensor data
while True:
    temperature, humidity, co2_level = generate_random_sensor_values()
    sensor_data_history.append((temperature, humidity, co2_level))  # Log data
    
    # Keep only recent data to limit memory usage
    if len(sensor_data_history) > 720:  # Retain up to 5 hours of data at 5-second intervals
        sensor_data_history.pop(0)  # Remove the oldest data point
    
    send_data_to_thingspeak(temperature, humidity, co2_level)
    print(f"Data Sent: Temperature={temperature:.2f}°C, Humidity={humidity:.2f}%, CO2 Level={co2_level:.2f}ppm")
    time.sleep(5)  # Interval between data transmissions (adjust as needed)
