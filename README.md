

# 🍎 Computer Vision Assignment 02

## Otsu's Thresholding & Region Growing Segmentation

This project demonstrates two essential image processing techniques using Python:

* 📌 **Otsu's Thresholding**: Automatic threshold selection for binarizing noisy images.
* 📌 **Region Growing Segmentation**: Interactive segmentation based on pixel intensity similarity.

All outputs are visualized and saved automatically in the project folder.

---

## 🚀 Technologies Used

* 🐍 Python 3
* 📦 OpenCV
* 📦 NumPy
* 📦 Matplotlib
* 📦 skimage

---

## 📂 Project Files

| File                             | Description                         |
| -------------------------------- | ----------------------------------- |
| `computer_vision_Ass_02_4023.py` | Main Python script                  |
| `fruitsample.png`                | Sample input image                  |
| `output/`                        | Folder containing all result images |

---

## 🛠️ Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/KirushnanKithurshika/Computer_Vision_Ass02_4023.git
   ```
2. **Navigate to Project Folder:**

   ```bash
   cd Computer_Vision_Ass02_4023
   ```
3. **Install Required Libraries:**

   ```bash
   pip install opencv-python numpy matplotlib scikit-image
   ```
4. **Run the Python Script:**

   ```bash
   python computer_vision_Ass_02_4023.py
   ```
5. **Select Seed Point:**
   When the noisy grayscale image appears, click on any point to start region growing.

---

## 🎯 Features

✅ Load and display color and grayscale images
✅ Add Gaussian noise to the image
✅ Apply Otsu's Thresholding for binarization
✅ Interactive seed selection for region growing
✅ Segment regions based on intensity similarity
✅ Save all output images automatically

---

## 📸 Output Samples

* 🖼️ Original Image (Color)
* 🖤 Original Image (Grayscale)
* 🎨 Noisy Color Image
* ⚫ Noisy Grayscale Image
* ⚙️ Otsu Thresholding Result
* 🌱 Region Growing Segmentation Result

*All results are saved in the `output` folder.*

---

## 📝 Notes

* Make sure your input image is named **`fruitsample.png`**.
* You can adjust:

  * Noise level: Change `sigma` value in the script.
  * Region Growing sensitivity: Change the threshold value.

---

## 👩‍💻 Author

**Kithurshika Kirushnan**
University of Ruhuna – Computer Vision Assignment 02

---

## ⭐️ Feel free to star the repository if you found it useful!

---

If you want, I can help you further customize this with badges (build passing, Python version, etc.) or help you create a repository banner. Let me know! 😊
