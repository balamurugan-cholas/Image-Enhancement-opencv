<<<<<<< HEAD

# 🖼️ Image Enhancement Web App using Flask + OpenCV

This is a web-based application built with **Flask** and **OpenCV** that allows users to upload images and apply image enhancement filters such as **Gaussian Blur**, **Median Blur**, and **Bilateral Filter** with custom intensity levels.

---

## 🌐 Live Demo

> [🔗 Live Demo](https://image-enhancer.onrender.com)

---

## 💡 Features

- 📤 Upload an image via browser  
- 🎛️ Choose from 3 filters:
  - Gaussian Blur
  - Median Blur
  - Bilateral Filter  
- 🔧 Adjust intensity manually  
- ⚡ Enhanced image shown alongside original  
- 🧠 Powered by OpenCV, served with Flask  

---

## 🛠️ Tech Stack

| Technology   | Purpose                    |
|--------------|-----------------------------|
| Python 3.x   | Core language               |
| Flask        | Web server framework        |
| OpenCV       | Image filtering & processing|
| HTML/CSS     | Frontend interface          |
| Bootstrap    | Styling & responsiveness    |

---

## 📁 Folder Structure

```
image-enhancement-app/
│
├── app.py
├── templates/
│   └── home.html
├── static/
│   ├── uploads/        # For uploaded images
│   └── fixed/          # For processed images
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run Locally

1. **Clone the Repository**

```
git clone https://github.com/yourusername/image-enhancement-app.git
cd image-enhancement-app
```

2. **Create a virtual environment (optional)**

```
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
```

3. **Install Dependencies**

```
pip install -r requirements.txt
```

Or install directly:

```
pip install Flask==2.3.3 opencv-python==4.9.0.80 numpy==1.26.4
```

4. **Run the App**

```
python app.py
```

5. Open your browser and go to:  
`http://127.0.0.1:3000`

---

## 🧪 Available Filters

| Filter           | Description                                        |
|------------------|----------------------------------------------------|
| Gaussian Blur     | Applies a Gaussian kernel for smooth blur         |
| Median Blur       | Reduces noise while preserving edges              |
| Bilateral Filter  | Smooths while keeping edge sharpness              |

Each filter can be adjusted by intensity input on the frontend.

---

## ⚙️ Requirements

```
Flask==2.3.3  
opencv-python==4.9.0.80  
numpy==1.26.4
```

To install:

```
pip install Flask==2.3.3 opencv-python==4.9.0.80 numpy==1.26.4
```

---

## 📬 Author

**Balamurugan Cholan**  
[GitHub](https://github.com/balamurugan-cholan)  
[LinkedIn](https://linkedin.com/in/yourprofile)  
[Instagram](https://instagram.com/yourprofile)

---

This project is open source.

---

> 💡 A simple and clean interface for real-time image enhancement.  
> Built with ❤️ using Flask and OpenCV.
=======
# Image-Enhancement-opencv
A simple Flask-based web app that allows users to upload images and apply real-time enhancements using OpenCV filters like Gaussian Blur, Median Blur, and Bilateral Filter. Ideal for quick demos of image preprocessing techniques in image processing projects.
>>>>>>> a91cef51aceafb690dfa3c74147d4f01abeab250
