# IOT-ThinkSpeak-and-Wokwi

This is assignment 3 of the IOT - App Development course.

The assignment is designed to learn how to collect and transmit simulated environmental sensor data to ThingSpeak, a cloud-based service for IoT (Internet of Things) projects. This script simulates data for temperature, humidity, and CO2 levels, then publishes this data to a specified ThingSpeak channel using MQTT (Message Queuing Telemetry Transport), a lightweight messaging protocol for small sensors and mobile devices. 

Steps -
1. Make accounts on both Wokwi and ThingSpeak
2. Add a channel on Thingspeak with 3 fields.
3. Add a device on ThingSpeak and add it to the channel.
4. Copy and paste the code provided here in the WokWi interface (Device = micropython-esp32).
5. Change the mqtt_client_id, mqtt_username, mqtt_password paramters in the code by copying them from device details in ThingSpeak.
6. Change the channel id, with your channel id in the topic_temperature, topic_humidity, topic_co2_level paramters.
7. Run the code.
8. You should see you results in the private tab of the channel.
