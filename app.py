from flask import Flask, render_template, redirect, request, url_for
import numpy as np
import cv2 as cv
import os

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/upload_image', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        file = request.files['image']
        selected_filter = request.form.get('enhancement')
        intensity = int(request.form.get('intensity'))
        
        filename = file.filename
        filepath = os.path.join('static', 'uploads', filename)
        file.save(filepath)

        img = cv.imread(filepath)
        filter = cv.GaussianBlur(img, (5, 5), intensity) if selected_filter == 'GaussianBlur' else \
                 cv.medianBlur(img, intensity) if selected_filter == 'MedianBlur' else \
                 cv.bilateralFilter(img, intensity, 75, 75) if selected_filter == 'BilateralFilter' else \
                 img

        fixed_path = os.path.join('static', 'fixed', filename)
        cv.imwrite(fixed_path, filter)

        return render_template('home.html', image=filepath, enhanced_image=fixed_path)
    return render_template('home.html', image="", enhanced_image="")

if __name__ == '__main__':
    app.run(debug=True, port=3000)