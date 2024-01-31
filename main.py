from flask import Flask,make_response
import random
import udp_server
import threading

app=Flask(__name__)
@app.route('/port')
def generate_random_port():
    port=random.randint(1024,65535)
    response= make_response(str(port))
    response.headers['Port-Number']=str(port)
    udp_thread = threading.Thread(target=udp_server.udp_server, args=(port,))
    udp_thread.start()


    return response
if __name__ == '__main__':
    app.run(debug=True)


