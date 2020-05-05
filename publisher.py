import paho.mqtt.client as paho

def on_connect(client, userdata, flags, rc):
    print("CONNACK received with code %d." % (rc))

def on_publish(client, userdata, mid):
    print("mid: "+str(mid))

def on_disconnect(client, userdata, rc):
    print("Disconnected")


def main():
    client = paho.Client()
    client.on_connect = on_connect
    client.connect("broker.hivemq.com", 1883)
    client.on_publish = on_publish
    client.on_disconnect = on_disconnect
    #playsound("clapping.wav")
    client.loop_start()

    while True:
        print("1. Clap")
        print("2. Horn")
        print("3. Dog")
        print("4. URL")
        choice = input("Select: ")
        if choice == "1":
            msg_info = client.publish("mqtt11/a", "1", qos=1)
        if choice == "2":
            msg_info = client.publish("mqtt11/b", "2", qos=1)
        if choice == "3":
            msg_info = client.publish("mqtt11/c", "3", qos=1)
        if choice == "4":
            url = input("Enter url: ")
            msg_info = client.publish("mqtt11/browse", url, qos=1)

        # This call will block until the message is published.
        msg_info.wait_for_publish()


if __name__ == '__main__':
    main()
