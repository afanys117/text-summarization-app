from flask import Flask, render_template, request, jsonify
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

app = Flask(__name__)

model_name = "./model"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    input_text = request.json.get('text')

    inputs = tokenizer("summarize: " + input_text, return_tensors="pt", max_length=128, truncation=True)['input_ids']

    summary_ids = model.generate(inputs, max_new_tokens=100, do_sample=False)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)
