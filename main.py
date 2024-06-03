from flask import Flask, render_template, request
from phish import check_url_legitimacy
import pickle
from keras.models import load_model
from keras.preprocessing import sequence

app = Flask(__name__)

# Load tokenizer
with open('tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

# Load the trained model
model = load_model('trained_cnn_model.h5')

# Maximum sequence length
MAX_SEQUENCE_LENGTH = 2000

@app.route('/')
def home():
    return render_template('interface.html')

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form['url']
    result = check_url_legitimacy(url, model, tokenizer, MAX_SEQUENCE_LENGTH)
    return render_template('interface.html', prediction=result, url=url)

if __name__ == '__main__':
    app.run(debug=True)
