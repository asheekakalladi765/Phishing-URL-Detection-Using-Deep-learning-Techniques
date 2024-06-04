# Phishing-URL-Detection-Using-Deep-learning-Techniques
Phishing URL detection using deep learning is highly relevant due to the increasing sophistication of phishing attacks, which pose significant cybersecurity threats. Traditional rule-based methods struggle to keep up, whereas deep learning models excel by automatically extracting features from vast datasets, adapting to new tactics, and providing real-time, scalable, and accurate detection.

 In this project, CNNs, LSTMs, and GRUs were employed to analyze and detect phishing URLs. Among these, CNNs achieved the highest accuracy at 90%, surpassing the performance of LSTMs and GRUs. This demonstrates the effectiveness of CNNs in capturing and analyzing the spatial features of URLs, making them particularly well-suited for this type of task.

 Further created a tokenizer and saved it as a tokenizer.pkl file. This tokenizer preprocesses the input URLs by converting them into a format suitable for the CNN model, ensuring consistent and accurate tokenization for any new data the model encounters.

Then saved the trained CNN model as a cnn_model.h5 file. This file contains the architecture of the CNN model, its weights, and training configuration. By saving the model in this format, it can be easily loaded and leveraged within the user interface, allowing for real-time phishing URL detection.

To implement the user interface for the phishing URL detection project,Flask framework were used and created three files 'interface.html', 'main.py', and 'phish.py'. The interface.html file serves as the front-end, allowing users to input URLs. The main.py script sets up the Flask server, handles user requests, and displays results. The phish.py script loads the pre-trained CNN model (cnn_model.h5) and tokenizer (tokenizer.pkl), preprocesses URLs, and makes predictions.
