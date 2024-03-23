from flask import Flask, render_template, request, redirect, url_for
from main import process_image

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        # Get the uploaded file
        image_file = request.files['image']
        if image_file:
            # Save the file temporarily
            image_path = 'static/uploads/' + image_file.filename
            image_file.save(image_path)
            # Process the image
            input_image_path, output_image_path, result_count = process_image(image_path)
            # Redirect to the result page
            return redirect(url_for('result', input_image_path=input_image_path, output_image_path=output_image_path, result_count=result_count))
    # Redirect to the home page if there's an issue
    return redirect(url_for('home'))

@app.route('/result')
def result():
    input_image_path = request.args.get('input_image_path')
    output_image_path = request.args.get('output_image_path')
    result_count = request.args.get('result_count')
    return render_template('result.html', input_image_path=input_image_path, output_image_path=output_image_path, result_count=result_count)

if __name__ == '__main__':
    app.run(debug=True)

