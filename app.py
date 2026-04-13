from flask import Flask, request, jsonify, render_template
import os
import threading
from flask_cors import CORS, cross_origin
from cnnClassifier.utils.common import decodeImage
from cnnClassifier.pipeline.prediction import PredictionPipeline



os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')




def run_training():
    os.system("python main.py")

@app.route("/train", methods=['GET','POST'])
@cross_origin()
def trainRoute():
    thread = threading.Thread(target=run_training)
    thread.start()
    return "Training started in the background!"



@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    filename = "inputImage.jpg"
    decodeImage(image, filename)
    
    # Create new PredictionPipeline object with the latest image
    prediction = PredictionPipeline(filename)
    result = prediction.predict()
    return jsonify(result)



if __name__ == "__main__":
    clApp = ClientApp()

    app.run(host='0.0.0.0', port=8080) #for GCP