import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Here you can subscribe to whatever topics you like
    # use '#' for a 'wildcard' - subscribe to any messages
    client.subscribe("Tish")
    
def on_message(client, userdata, msg):
    print(msg.topic + msg.payload.decode("utf-8") + "\n")

client = mqtt.Client()
client.connect("192.168.1.5", 1883, 60)

while True:
   message = input('Your message: ')
   new_message = '\033[1m' + '\033[93m' + message + '\033[0m'
   client.publish('Tish', new_message)


