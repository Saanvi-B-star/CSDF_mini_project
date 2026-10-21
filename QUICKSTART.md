# ⚡ Quick Start Guide

Get up and running in 5 minutes!

## 🎯 For Complete Beginners

### Step 1: Install Prerequisites (If not done)

#### Install Anaconda
1. Download from: https://www.anaconda.com/download
2. Run the installer
3. Follow installation wizard

#### Install Git
1. Download from: https://git-scm.com/downloads
2. Run the installer
3. Use default settings

---

### Step 2: Get the Project

#### Option A: Download ZIP (Easiest)
1. Go to GitHub repository
2. Click green **"Code"** button
3. Click **"Download ZIP"**
4. Extract to a folder (e.g., `C:\Projects\ImageForensics-Toolkit`)

#### Option B: Clone with Git (Recommended)
```bash
git clone https://github.com/yourusername/ImageForensics-Toolkit.git
cd ImageForensics-Toolkit
```

---

### Step 3: Set Up Environment

**Open Anaconda Prompt:**
- Windows: Press **Win key**, type "Anaconda Prompt"
- Mac/Linux: Open Terminal

**Run these commands:**
```bash
# Create environment
conda create -n forensics python=3.10 -y

# Activate it
conda activate forensics

# Navigate to project folder
cd path/to/ImageForensics-Toolkit

# Install requirements
pip install -r requirements.txt
```

---

### Step 4: Run the Application

```bash
python main.py
```

**That's it! The application should launch! 🎉**

---

## 🚀 Quick Usage Guide

### Basic Workflow:

1. **Click "Select Image"** → Choose any image file
2. **Click "Extract Metadata"** → See EXIF data
3. **Click "Calculate Hash"** → Get hash values
4. **Click "ELA Analysis"** → Detect manipulation
5. **Click "Export Report"** → Save your analysis

---

## 🎨 Supported Image Formats

✅ JPEG/JPG  
✅ PNG  
✅ BMP  
✅ TIFF  
✅ GIF  

---

## 📁 Project Structure Overview

```
ImageForensics-Toolkit/
│
├── main.py                 ← Main application (run this)
├── requirements.txt        ← Python packages needed
├── README.md              ← Full documentation
├── SETUP_GUIDE.md         ← Detailed setup instructions
└── .gitignore             ← Git ignore rules
```

---

## 🐛 Common Issues & Quick Fixes

### Issue: "conda not recognized"
**Fix:** Restart Anaconda Prompt as Administrator

### Issue: "tkinter not found"
**Fix:**
```bash
conda install tk
```

### Issue: "Permission denied"
**Windows Fix:** Run Anaconda Prompt as Administrator  
**Mac/Linux Fix:** Use `sudo pip install -r requirements.txt`

### Issue: Application won't start
**Fix:**
```bash
# Make sure environment is activated
conda activate forensics

# Reinstall requirements
pip install -r requirements.txt --force-reinstall
```

---

## 📋 Daily Use Checklist

Every time you want to use the tool:

```bash
# 1. Open Anaconda Prompt/Terminal
# 2. Activate environment
conda activate forensics

# 3. Navigate to project
cd path/to/ImageForensics-Toolkit

# 4. Run application
python main.py

# 5. When done, deactivate (optional)
conda deactivate
```

---

## 🎓 For Your University Project

### Before Submission:

- [ ] Update README.md with your name and roll number
- [ ] Fill in PROJECT_REPORT_TEMPLATE.md
- [ ] Test all features work correctly
- [ ] Take screenshots of the application
- [ ] Create a demo video (optional but impressive)
- [ ] Push code to GitHub
- [ ] Make repository public
- [ ] Add project documentation

### GitHub Repository Setup:

1. **Create Repository:**
   - Go to github.com
   - Click **"New repository"**
   - Name: `ImageForensics-Toolkit`
   - Make it **Public**
   - Click **"Create repository"**

2. **Push Your Code:**
```bash
cd ImageForensics-Toolkit
git init
git add .
git commit -m "Initial commit: Digital Forensics Image Analysis Tool"
git branch -M main
git remote add origin https://github.com/yourusername/ImageForensics-Toolkit.git
git push -u origin main
```

3. **Share Repository Link:**
   - Copy the repository URL
   - Include it in your project report
   - Share with your instructor

---

## 📸 Demo Images for Testing

You can test with:
- Any photo from your phone
- Downloaded images from internet
- Screenshots
- Sample forensic images (search online)

**Pro Tip:** For ELA testing, try:
1. Original unedited photo (should show uniform ELA)
2. Photo edited in Photoshop/GIMP (should show bright spots)

---

## 💡 Pro Tips

1. **Create Desktop Shortcut:**
   - Create a `.bat` file (Windows) or `.sh` file (Mac/Linux)
   - Add the activation and run commands
   - Double-click to launch

2. **Keep Environment Clean:**
   - Only install required packages
   - Don't modify core files unnecessarily

3. **Regular Backups:**
   - Commit changes to Git regularly
   - Push to GitHub often

4. **Document Everything:**
   - Take screenshots during development
   - Note any challenges faced
   - Document solutions found

---

## 🎯 Next Steps

Once you're comfortable with the basics:

1. **Explore the Code:**
   - Open `main.py` in a text editor
   - Read through the comments
   - Understand the functions

2. **Customize:**
   - Change colors/themes
   - Add your university logo
   - Modify window title

3. **Extend Features:**
   - Add more analysis methods
   - Improve the UI
   - Add batch processing

4. **Learn More:**
   - Read digital forensics resources
   - Study EXIF standards
   - Learn about image manipulation detection

---

## 📞 Need Help?

1. **Check Documentation:**
   - README.md (overview)
   - SETUP_GUIDE.md (detailed setup)
   - PROJECT_REPORT_TEMPLATE.md (project report)

2. **Common Resources:**
   - Python Documentation: https://docs.python.org/
   - Tkinter Tutorial: https://realpython.com/python-gui-tkinter/
   - OpenCV Docs: https://docs.opencv.org/

3. **Ask for Help:**
   - Create GitHub Issue
   - Ask your instructor
   - Consult with classmates

---

## ✅ Success Checklist

After setup, you should be able to:

- [x] Launch the application
- [x] Load an image
- [x] See all tabs (Basic Info, Metadata, Hash, Forensic)
- [x] Extract metadata successfully
- [x] Calculate hash values
- [x] Perform ELA analysis
- [x] Export reports (TXT and JSON)
- [x] Clear and reload images

**All checked? You're ready to go! 🎉**

---

## 🏆 Bonus: Impress Your Evaluator

1. **Add Screenshots to README:**
   - Take professional screenshots
   - Add them to README.md

2. **Create Demo Video:**
   - Record screen while using tool
   - Show all features
   - Upload to YouTube (unlisted)

3. **Prepare Presentation:**
   - PPT with architecture diagrams
   - Live demo during presentation
   - Show code snippets

4. **Additional Documentation:**
   - User manual
   - Technical documentation
   - Test cases report

---

## 🎊 You're All Set!

**Time to complete setup:** ~10 minutes  
**Time to understand basics:** ~30 minutes  
**Ready to demonstrate:** ✅

**Good luck with your project!** 🚀

---

**Quick Command Reference Card:**

```bash
# Setup (one-time)
conda create -n forensics python=3.10 -y
conda activate forensics
pip install -r requirements.txt

# Daily Use
conda activate forensics
python main.py

# Update packages
pip install -r requirements.txt --upgrade

# Deactivate when done
conda deactivate
```

**Save this command card for quick reference!**