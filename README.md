# 🔍 Digital Forensics - Image Analysis Tool

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)

**A comprehensive digital forensics tool for image analysis and manipulation detection**

</div>

---

## 📋 Project Information

- **Subject**: Cyber Security and Digital Forensics
- **Subject Code**: 410244
- **University**: Savitribai Phule Pune University
- **Project Type**: Mini-Project
- **Language**: Python 3.8+

---

## 🎯 Features

### 🔐 Core Forensic Capabilities

1. **Metadata Extraction**
   - Complete EXIF data extraction
   - GPS coordinates (if available)
   - Camera information
   - Date/time stamps
   - Software information

2. **Hash Value Calculation**
   - MD5 hash generation
   - SHA-1 hash generation
   - SHA-256 hash generation
   - File integrity verification

3. **Error Level Analysis (ELA)**
   - Detects image manipulation
   - Identifies edited regions
   - Visual representation of compression inconsistencies
   - Helps identify copy-paste forgeries

4. **Basic File Analysis**
   - File size and format detection
   - Image dimensions
   - Color mode analysis
   - Creation/modification timestamps

5. **Report Generation**
   - Export analysis to TXT format
   - Export analysis to JSON format
   - Comprehensive forensic reports
   - Chain of custody documentation

---

## 🛠️ Technology Stack

- **Python 3.8+**: Core programming language
- **Tkinter**: GUI framework (included with Python)
- **Pillow (PIL)**: Image processing library
- **OpenCV**: Computer vision and ELA analysis
- **piexif**: Advanced EXIF metadata handling
- **NumPy**: Numerical computations
- **Git/GitHub**: Version control

---

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- Anaconda (as mentioned you have it installed)
- Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/ImageForensics-Toolkit.git
cd ImageForensics-Toolkit
```

### Step 2: Create Conda Environment (Recommended)

```bash
# Create a new conda environment
conda create -n forensics python=3.10 -y

# Activate the environment
conda activate forensics
```

### Step 3: Install Dependencies

```bash
# Install required packages
pip install -r requirements.txt
```

### Alternative: Using Anaconda Navigator

1. Open Anaconda Navigator
2. Go to Environments
3. Create new environment named "forensics"
4. Open terminal in that environment
5. Navigate to project folder and run: `pip install -r requirements.txt`

---

## 🚀 Usage

### Running the Application

```bash
# Make sure you're in the project directory and environment is activated
python main.py
```

### Using the Tool

1. **Select Image**: Click "Select Image" button to load an image file
2. **Extract Metadata**: View complete EXIF and metadata information
3. **Calculate Hash**: Generate cryptographic hashes for file verification
4. **ELA Analysis**: Perform Error Level Analysis to detect manipulation
5. **Export Report**: Save your analysis results to a file
6. **Clear**: Reset the tool for a new analysis

---

## 📸 Screenshots

### Main Interface
The tool features a modern, user-friendly interface with:
- Image preview panel
- Tabbed analysis results
- One-click forensic operations
- Professional forensic report generation

---

## 🔬 Technical Details

### Error Level Analysis (ELA)
ELA works by resaving an image at a known quality level and comparing it to the original. Areas with different error levels can indicate:
- Image manipulation
- Copy-paste forgeries
- Cloned regions
- Recently added elements

### Hash Values
The tool generates three types of cryptographic hashes:
- **MD5**: Fast but less secure (128-bit)
- **SHA-1**: Moderate security (160-bit)
- **SHA-256**: Most secure for forensics (256-bit)

### Metadata Analysis
Extracts comprehensive EXIF data including:
- Camera make and model
- GPS coordinates
- Exposure settings
- Software used
- Timestamps

---

## 📂 Project Structure

```
ImageForensics-Toolkit/
│
├── main.py                 # Main application file
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore rules
├── README.md              # Project documentation
├── LICENSE                # MIT License
│
├── docs/                  # Documentation (optional)
│   ├── user_manual.pdf
│   └── technical_report.pdf
│
├── samples/               # Sample images for testing (optional)
│   ├── original.jpg
│   └── manipulated.jpg
│
└── reports/               # Generated reports (gitignored)
    └── analysis_*.txt
```

---

## 🎓 Academic Context

### Learning Objectives

This project demonstrates understanding of:

1. **Digital Forensics Principles**
   - Evidence preservation
   - Chain of custody
   - File integrity verification

2. **Image Analysis Techniques**
   - Metadata examination
   - Cryptographic hashing
   - Manipulation detection

3. **Software Development**
   - GUI design
   - Python programming
   - Version control with Git

4. **Cyber Security Concepts**
   - Data integrity
   - File authentication
   - Evidence documentation

---

## 🤝 Contributing

This is an academic project, but contributions and suggestions are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 Future Enhancements

- [ ] Add support for batch processing multiple images
- [ ] Implement copy-move forgery detection
- [ ] Add noise analysis
- [ ] Include thumbnail analysis
- [ ] Database integration for case management
- [ ] Add PDF report generation
- [ ] Implement reverse image search
- [ ] Add more forensic algorithms (JPEG Ghost, etc.)

---

## ⚖️ Legal Disclaimer

This tool is developed for educational and research purposes as part of an academic project. Users are responsible for ensuring they have proper authorization before analyzing any images. Always comply with local laws and regulations regarding digital forensics and privacy.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**[Your Name]**
- Roll Number: [Your Roll Number]
- Subject: Cyber Security and Digital Forensics (410244)
- University: Savitribai Phule Pune University

---

## 📞 Support

For questions or issues:
- Create an issue on GitHub
- Contact: [your.email@example.com]

---

## 🙏 Acknowledgments

- Savitribai Phule Pune University
- Department of Computer Engineering
- Course Instructor: [Instructor Name]
- All open-source contributors whose libraries made this project possible

---

## 📚 References

1. **Digital Forensics Fundamentals**
   - Forensic Image Analysis Techniques
   - EXIF Metadata Standards
   - Cryptographic Hash Functions

2. **Image Manipulation Detection**
   - Error Level Analysis (ELA)
   - Copy-Move Forgery Detection
   - JPEG Compression Analysis

3. **Python Libraries Documentation**
   - Pillow: https://pillow.readthedocs.io/
   - OpenCV: https://opencv.org/
   - piexif: https://piexif.readthedocs.io/

---
