# Blur2Sharp_Textile
# 🔍 Blur2Sharp

Blur2Sharp is a powerful and easy-to-use **image sharpening and background replacement web app**, built using **Streamlit** and **OpenCV**, enhanced with **background removal** using `rembg`. It allows users to upload blurry images (e.g., from surveillance or textile inspections), sharpen them, preview with new backgrounds, compare original vs. sharpened versions, and download results.

---

## ✨ Features

- 🔧 **Customizable sharpening intensity**
- 🖼️ **Compare original vs. sharpened images**
- 🚫 **Remove background** using `rembg`
- 🌄 **Apply image to 5+ preset backgrounds**
- 📥 **Download all variants as ZIP**
- 🎨 **Dark/Light theme toggle**
- 🔁 **Reset functionality**
- 📸 **Download sharpened image directly**

---

## 🚀 Demo

Coming soon on Streamlit Cloud / HuggingFace Space

---

## 📁 Project Structure

blur2sharp_app/
│
├── app.py # Main Streamlit application
├── requirements.txt # Python dependencies
│
├── utils/
│ ├── sharpen.py # Image sharpening logic
│ └── background.py # Background removal & overlay
│
├── static/
│ ├── sample_blur/ # Sample input images
│ └── backgrounds/ # Preset background images

 2. Set Up Virtual Environment
    python -m venv tenv
    source tenv/bin/activate   # On Windows: tenv\Scripts\activate
3. Install Dependencies
   pip install -r requirements.txt
4. Run the App
   streamlit run app.py

🧠 How It Works
🔸 Image Sharpening
Uses OpenCV’s kernel convolution:
kernel = np.array([
    [0, -1, 0],
    [-1, intensity + 4, -1],
    [0, -1, 0]
]) / (intensity + 1)
The intensity is controlled via a slider. Higher values create stronger sharpening.

🔸 Background Removal
We use the rembg library (based on U2Net) to remove the background from the uploaded image.

🔸 Background Overlay
After background is removed, we paste the transparent subject on top of each preset background image and generate previews.

🧪 Optional Enhancements (Future Work)
Deblurring using SwinIR GAN model

User-uploaded background support

Add watermark/signature to output

Deploy on Streamlit Cloud, HuggingFace Spaces, or Render

👤 Author
Kundan Yadav
Email: ky4910917@gmail.com



