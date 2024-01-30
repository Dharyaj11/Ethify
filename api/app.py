from flask import Flask, jsonify, request
from flask_cors import CORS
from joblib import load

detect_classifier = load('detect_classifier.joblib')
detect_vect = load('detect_vectorizer.joblib')
classify_classifier = load('classify_classifier.joblib')
classify_vect = load('classify_vectorizer.joblib')
# cookie_classifier = load('cookie_classifier.joblib')
# cookie_vect = load('cookie_vectorizer.joblib')
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def main():
    if request.method == 'POST':
        outputResult = []
        reqData = request.get_json().get('tokens')

        for tokenData in reqData:
            recon = detect_classifier.predict(detect_vect.transform([tokenData]))
            if recon == 'Dark':
                classify = classify_classifier.predict(classify_vect.transform([tokenData]))
                outputResult.append(classify[0])
            else:
                outputResult.append(recon[0])

        darkResult = [reqData[i] for i in range(len(outputResult)) if outputResult[i] == 'Dark']
        for i in darkResult:
            print(i)
        print()
        print(len(darkResult))

        msg = '{ \'recon\': ' + str(outputResult) + ' }'
        print(msg)

        json = jsonify(msg)

        return json

if __name__ == '__main__':
    app.run(threaded=True, debug=True)

