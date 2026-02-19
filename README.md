\# 🚀 Pro-Image-Compressor CLI



!\[Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge\&logo=python)

!\[License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

!\[Maintained](https://img.shields.io/badge/Maintained%3F-yes-brightgreen?style=for-the-badge)



\*\*Pro-Image-Compressor\*\* is a modern, high-speed Command Line Interface (CLI) tool designed to compress single or batch images without sacrificing significant quality. Built for developers and creators who want to reclaim storage space and optimize web assets instantly.



---



\## ✨ Features



\* \*\*Batch Processing:\*\* Scan and compress entire folders (`.jpg`, `.jpeg`, `.png`, `.webp`) with a single command.

\* \*\*Live Progress Tracking:\*\* Integrated with `tqdm` to provide real-time visual feedback.

\* \*\*Smart Conversion:\*\* Automatically handles color profiles (RGBA to RGB) during format transitions.

\* \*\*Performance Report:\*\* Generates a sleek statistical table showing exactly how much storage you saved per file.

\* \*\*Lightweight \& Fast:\*\* Powered by the Pillow library with optimized memory management.



---



\## 📸 Preview



```text

🚀 Starting optimization: 12 files found.

Compressing: 100%|████████████████████████████████| 12/12 \[00:02<00:00, 5.42img/s]



============================================================

FILENAME                  | ORIGINAL   | OPTIMIZED  | SAVED

============================================================

vacation\_photo.jpg        | 4.52MB     | 1.12MB     | 75.2%

profile\_picture.png       | 850.12KB   | 210.45KB   | 75.2%

...

============================================================

Total Storage Saved: 15.42MB

============================================================



\## 🛠️ Installation \& Setup



Follow these steps to get the project running on your local machine:



1\. \*\*Clone the repository:\*\*

&nbsp;  ```bash

&nbsp;  git clone \[https://github.com/wenshert-dev/pro-image-compressor.git](https://github.com/wenshert-dev/pro-image-compressor.git)

&nbsp;  cd pro-image-compressor



2\. Create a virtual environment (Optional but Recommended):

```bash

python -m venv venv

\# On Windows:

.\\venv\\Scripts\\activate

\# On Mac/Linux:

source venv/bin/activate



3\. Install the required libraries:

```bash

pip install -r requirements.txt



4\. Verify the installation:

```bash

python compressor.py --help


\#🚀 Usage

Basic compression (Default quality: 70):
```bash
python compressor.py -i ./my_images -o ./optimized_results

Run with custom quality settings:
```bash
python compressor.py -i ./my_images -q 50

Parameters:

Parameter,Description,Default
"-i, --input",Input folder path,. (Current directory)
"-o, --output",Output folder path,compressed
"-q, --quality",Compression quality (1-95),70


🤝 Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

1. Fork the Project.
2. Create your Feature Branch (git checkout -b feature/AmazingFeature).
3. Commit your Changes (git commit -m 'Add some AmazingFeature').
4. Push to the Branch (git push origin feature/AmazingFeature).
5. Open a Pull Request.


📄 License
Distributed under the MIT License. See LICENSE for more information.
Developed by: wenshert-dev





