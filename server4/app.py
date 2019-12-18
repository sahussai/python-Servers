import random
from flask import Flask, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


class Server:

    def __setTemperature(self):
        self.temperature = round(random.uniform(19, 35), 2)

    def __setUploadSpeed(self):
        self.uploadSpeed = round(random.uniform(33, 70), 2)

    def __setDownloadSpeed(self):
        self.downloadSpeed = round(random.uniform(33, 70), 2)

    def __init__(self, name):
        self.name = name
        self.status = "OK"
        self.__setTemperature()
        self.__setUploadSpeed()
        self.__setDownloadSpeed()

    def reinitialize(self):
        self.__setTemperature()
        self.__setUploadSpeed()
        self.__setDownloadSpeed()

    def getInfo(self):
        return {
            "name": self.name,
            "status": self.status,
            "temperature": self.temperature,
            "uploadSpeed": self.uploadSpeed,
            "downloadSpeed": self.downloadSpeed
        }


@app.route('/')
def initialize():

    serv1 = Server("Server4")
    # print(serv1.getInfo())

    # return serv1.getInfo()
    return jsonify({
        "message": "You have reached " + serv1.name + " .",
        "data": serv1.getInfo()
    })


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
