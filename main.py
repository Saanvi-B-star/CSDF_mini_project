"""
Digital Forensics Image Analysis Tool
Subject: Cyber Security and Digital Forensics (410244)
University: Savitribai Phule Pune University
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
from PIL import Image, ImageTk, ExifTags
import hashlib
import os
from datetime import datetime
import json
from pathlib import Path
import piexif
import cv2
import numpy as np

class ImageForensicsTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Forensics - Image Analysis Tool")
        self.root.geometry("1200x800")
        self.root.configure(bg='#2c3e50')
        
        self.current_image_path = None
        self.original_image = None
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main container
        main_frame = tk.Frame(self.root, bg='#2c3e50')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title
        title_label = tk.Label(
            main_frame, 
            text="Digital Forensics - Image Analysis Tool",
            font=('Arial', 20, 'bold'),
            bg='#2c3e50',
            fg='white'
        )
        title_label.pack(pady=10)
        
        # Control Panel
        control_frame = tk.Frame(main_frame, bg='#34495e', relief=tk.RAISED, borderwidth=2)
        control_frame.pack(fill=tk.X, pady=10)
        
        btn_style = {
            'font': ('Arial', 10, 'bold'),
            'bg': '#3498db',
            'fg': 'white',
            'activebackground': '#2980b9',
            'cursor': 'hand2',
            'padx': 20,
            'pady': 10
        }
        
        tk.Button(control_frame, text="Select Image", command=self.select_image, **btn_style).pack(side=tk.LEFT, padx=5, pady=10)
        tk.Button(control_frame, text="Extract Metadata", command=self.extract_metadata, **btn_style).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Calculate Hash", command=self.calculate_hash, **btn_style).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="ELA Analysis", command=self.ela_analysis, **btn_style).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Export Report", command=self.export_report, **btn_style).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Clear", command=self.clear_all, bg='#e74c3c', fg='white', font=('Arial', 10, 'bold'), padx=20, pady=10).pack(side=tk.LEFT, padx=5)
        
        # Content area with two columns
        content_frame = tk.Frame(main_frame, bg='#2c3e50')
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Left panel - Image display
        left_panel = tk.Frame(content_frame, bg='#34495e', relief=tk.RAISED, borderwidth=2)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        tk.Label(left_panel, text="Image Preview", font=('Arial', 12, 'bold'), bg='#34495e', fg='white').pack(pady=5)
        
        self.image_label = tk.Label(left_panel, bg='#2c3e50', text="No image loaded", fg='gray', font=('Arial', 12))
        self.image_label.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Right panel - Analysis results
        right_panel = tk.Frame(content_frame, bg='#34495e', relief=tk.RAISED, borderwidth=2)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))
        
        tk.Label(right_panel, text="Analysis Results", font=('Arial', 12, 'bold'), bg='#34495e', fg='white').pack(pady=5)
        
        # Notebook for tabs
        self.notebook = ttk.Notebook(right_panel)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Tab 1: Basic Info
        self.basic_info_text = scrolledtext.ScrolledText(
            self.notebook,
            wrap=tk.WORD,
            font=('Courier', 10),
            bg='#ecf0f1',
            fg='#2c3e50'
        )
        self.notebook.add(self.basic_info_text, text="Basic Info")
        
        # Tab 2: Metadata
        self.metadata_text = scrolledtext.ScrolledText(
            self.notebook,
            wrap=tk.WORD,
            font=('Courier', 10),
            bg='#ecf0f1',
            fg='#2c3e50'
        )
        self.notebook.add(self.metadata_text, text="Metadata")
        
        # Tab 3: Hash Values
        self.hash_text = scrolledtext.ScrolledText(
            self.notebook,
            wrap=tk.WORD,
            font=('Courier', 10),
            bg='#ecf0f1',
            fg='#2c3e50'
        )
        self.notebook.add(self.hash_text, text="Hash Values")
        
        # Tab 4: Forensic Analysis
        self.forensic_text = scrolledtext.ScrolledText(
            self.notebook,
            wrap=tk.WORD,
            font=('Courier', 10),
            bg='#ecf0f1',
            fg='#2c3e50'
        )
        self.notebook.add(self.forensic_text, text="Forensic Analysis")
        
        # Status bar
        self.status_bar = tk.Label(
            main_frame,
            text="Ready",
            font=('Arial', 9),
            bg='#34495e',
            fg='white',
            anchor=tk.W,
            relief=tk.SUNKEN
        )
        self.status_bar.pack(fill=tk.X, side=tk.BOTTOM, pady=(10, 0))
    
    def select_image(self):
        file_path = filedialog.askopenfilename(
            title="Select an image",
            filetypes=[
                ("Image files", "*.jpg *.jpeg *.png *.bmp *.gif *.tiff"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            self.current_image_path = file_path
            self.load_image(file_path)
            self.display_basic_info()
            self.status_bar.config(text=f"Loaded: {os.path.basename(file_path)}")
    
    def load_image(self, path):
        try:
            self.original_image = Image.open(path)
            
            # Resize for display
            display_size = (400, 400)
            img_copy = self.original_image.copy()
            img_copy.thumbnail(display_size, Image.Resampling.LANCZOS)
            
            photo = ImageTk.PhotoImage(img_copy)
            self.image_label.config(image=photo, text="")
            self.image_label.image = photo
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {str(e)}")
    
    def display_basic_info(self):
        if not self.current_image_path:
            return
        
        try:
            file_stat = os.stat(self.current_image_path)
            file_size = file_stat.st_size
            
            info = f"""
╔══════════════════════════════════════════════════════════╗
║              BASIC FILE INFORMATION                      ║
╚══════════════════════════════════════════════════════════╝

File Name: {os.path.basename(self.current_image_path)}
File Path: {self.current_image_path}
File Size: {file_size:,} bytes ({file_size / 1024:.2f} KB)

Image Dimensions: {self.original_image.width} x {self.original_image.height} pixels
Image Format: {self.original_image.format}
Image Mode: {self.original_image.mode}

Created: {datetime.fromtimestamp(file_stat.st_ctime).strftime('%Y-%m-%d %H:%M:%S')}
Modified: {datetime.fromtimestamp(file_stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S')}
Accessed: {datetime.fromtimestamp(file_stat.st_atime).strftime('%Y-%m-%d %H:%M:%S')}
"""
            
            self.basic_info_text.delete(1.0, tk.END)
            self.basic_info_text.insert(1.0, info)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to get basic info: {str(e)}")
    
    def extract_metadata(self):
        if not self.current_image_path:
            messagebox.showwarning("Warning", "Please select an image first!")
            return
        
        try:
            img = Image.open(self.current_image_path)
            
            metadata = f"""
╔══════════════════════════════════════════════════════════╗
║              EXIF METADATA INFORMATION                   ║
╚══════════════════════════════════════════════════════════╝

"""
            
            exif_data = img._getexif()
            
            if exif_data:
                for tag_id, value in exif_data.items():
                    tag = ExifTags.TAGS.get(tag_id, tag_id)
                    
                    if isinstance(value, bytes):
                        try:
                            value = value.decode()
                        except:
                            value = "<binary data>"
                    
                    metadata += f"{tag}: {value}\n"
            else:
                metadata += "No EXIF metadata found in this image.\n"
            
            # Try to get additional info using piexif
            try:
                exif_dict = piexif.load(self.current_image_path)
                
                metadata += "\n\n" + "="*60 + "\n"
                metadata += "DETAILED EXIF DATA (using piexif):\n"
                metadata += "="*60 + "\n\n"
                
                for ifd in ("0th", "Exif", "GPS", "1st"):
                    if ifd in exif_dict:
                        metadata += f"\n[{ifd} IFD]\n"
                        for tag in exif_dict[ifd]:
                            tag_name = piexif.TAGS[ifd][tag]["name"]
                            value = exif_dict[ifd][tag]
                            metadata += f"  {tag_name}: {value}\n"
            except:
                pass
            
            self.metadata_text.delete(1.0, tk.END)
            self.metadata_text.insert(1.0, metadata)
            
            self.status_bar.config(text="Metadata extracted successfully")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to extract metadata: {str(e)}")
    
    def calculate_hash(self):
        if not self.current_image_path:
            messagebox.showwarning("Warning", "Please select an image first!")
            return
        
        try:
            with open(self.current_image_path, 'rb') as f:
                file_data = f.read()
            
            md5_hash = hashlib.md5(file_data).hexdigest()
            sha1_hash = hashlib.sha1(file_data).hexdigest()
            sha256_hash = hashlib.sha256(file_data).hexdigest()
            
            hash_info = f"""
╔══════════════════════════════════════════════════════════╗
║              CRYPTOGRAPHIC HASH VALUES                   ║
╚══════════════════════════════════════════════════════════╝

These hash values can be used to verify file integrity and
detect any modifications to the original image.

MD5:
{md5_hash}

SHA-1:
{sha1_hash}

SHA-256:
{sha256_hash}

═══════════════════════════════════════════════════════════

FORENSIC NOTES:
- Hash values are unique fingerprints of the file
- Any modification will change these values
- Use for chain of custody and evidence verification
- SHA-256 is the most secure for forensic purposes
"""
            
            self.hash_text.delete(1.0, tk.END)
            self.hash_text.insert(1.0, hash_info)
            
            self.status_bar.config(text="Hash values calculated")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to calculate hash: {str(e)}")
    
    def ela_analysis(self):
        """Error Level Analysis - detects image manipulation"""
        if not self.current_image_path:
            messagebox.showwarning("Warning", "Please select an image first!")
            return
        
        try:
            # Read image
            img = cv2.imread(self.current_image_path)
            
            # Save with quality 95
            temp_path = "temp_ela.jpg"
            cv2.imwrite(temp_path, img, [cv2.IMWRITE_JPEG_QUALITY, 95])
            
            # Read compressed image
            compressed_img = cv2.imread(temp_path)
            
            # Calculate difference
            ela_img = cv2.absdiff(img, compressed_img)
            
            # Enhance the difference
            ela_img = cv2.convertScaleAbs(ela_img, alpha=10)
            
            # Convert to PIL Image for display
            ela_img_rgb = cv2.cvtColor(ela_img, cv2.COLOR_BGR2RGB)
            ela_pil = Image.fromarray(ela_img_rgb)
            
            # Display ELA image
            display_size = (400, 400)
            ela_pil.thumbnail(display_size, Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(ela_pil)
            self.image_label.config(image=photo)
            self.image_label.image = photo
            
            # Analysis results
            ela_result = f"""
╔══════════════════════════════════════════════════════════╗
║         ERROR LEVEL ANALYSIS (ELA) RESULTS               ║
╚══════════════════════════════════════════════════════════╝

ANALYSIS COMPLETED: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

INTERPRETATION GUIDE:
───────────────────────────────────────────────────────────

1. UNIFORM BRIGHTNESS:
   → Image is likely authentic
   → Consistent compression throughout

2. BRIGHT SPOTS/AREAS:
   → Possible manipulation or editing
   → Areas with different compression levels
   → May indicate copy-paste or cloning

3. SHARP EDGES WITH HIGH ELA:
   → Potential inserted objects
   → Recently added elements

4. DARK AREAS:
   → Heavily compressed regions
   → Possibly unmodified areas

═══════════════════════════════════════════════════════════

FORENSIC NOTES:
• ELA is not definitive proof of manipulation
• Consider other factors and analysis methods
• High quality original images may show minimal ELA
• Heavily edited images from editing software will show more

The ELA image is now displayed in the preview panel.
Bright areas indicate potential manipulation zones.

═══════════════════════════════════════════════════════════
"""
            
            self.forensic_text.delete(1.0, tk.END)
            self.forensic_text.insert(1.0, ela_result)
            
            # Cleanup
            if os.path.exists(temp_path):
                os.remove(temp_path)
            
            self.status_bar.config(text="ELA analysis completed")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to perform ELA analysis: {str(e)}")
    
    def export_report(self):
        if not self.current_image_path:
            messagebox.showwarning("Warning", "Please select an image first!")
            return
        
        try:
            save_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("JSON files", "*.json"), ("All files", "*.*")]
            )
            
            if save_path:
                report_data = {
                    "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    "basic_info": self.basic_info_text.get(1.0, tk.END),
                    "metadata": self.metadata_text.get(1.0, tk.END),
                    "hash_values": self.hash_text.get(1.0, tk.END),
                    "forensic_analysis": self.forensic_text.get(1.0, tk.END)
                }
                
                if save_path.endswith('.json'):
                    with open(save_path, 'w') as f:
                        json.dump(report_data, f, indent=4)
                else:
                    with open(save_path, 'w') as f:
                        f.write("="*80 + "\n")
                        f.write("DIGITAL FORENSICS - IMAGE ANALYSIS REPORT\n")
                        f.write("="*80 + "\n\n")
                        for key, value in report_data.items():
                            f.write(f"\n{'='*80}\n")
                            f.write(f"{key.upper().replace('_', ' ')}\n")
                            f.write(f"{'='*80}\n")
                            f.write(value)
                            f.write("\n")
                
                messagebox.showinfo("Success", f"Report exported to:\n{save_path}")
                self.status_bar.config(text=f"Report exported: {os.path.basename(save_path)}")
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export report: {str(e)}")
    
    def clear_all(self):
        self.current_image_path = None
        self.original_image = None
        self.image_label.config(image="", text="No image loaded", fg='gray')
        self.image_label.image = None
        
        self.basic_info_text.delete(1.0, tk.END)
        self.metadata_text.delete(1.0, tk.END)
        self.hash_text.delete(1.0, tk.END)
        self.forensic_text.delete(1.0, tk.END)
        
        self.status_bar.config(text="Cleared all data")

def main():
    root = tk.Tk()
    app = ImageForensicsTool(root)
    root.mainloop()

if __name__ == "__main__":
    main()