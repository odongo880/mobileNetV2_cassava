# 🌿 Cassava Disease Classifier - Streamlit Deployment Guide

A deep learning web application that classifies cassava leaf diseases using MobileNetV2.

## 📋 Prerequisites

1. **GitHub Account** - [Sign up here](https://github.com/join)
2. **Streamlit Cloud Account** - [Sign up here](https://streamlit.io/cloud) (free, uses GitHub login)
3. **Git installed locally** - [Download here](https://git-scm.com/downloads)
4. **Git LFS installed** - [Download here](https://git-lfs.github.com/) (required for large model files)

## 🚀 Deployment Steps

### Step 1: Install Git LFS (if not already installed)

```bash
# Download and install from https://git-lfs.github.com/
# Or use a package manager:

# Windows (using Chocolatey)
choco install git-lfs

# macOS
brew install git-lfs

# Initialize Git LFS
git lfs install
```

### Step 2: Create a GitHub Repository

1. Go to [GitHub](https://github.com) and create a new repository
2. Name it (e.g., `cassava-disease-classifier`)
3. Choose **Public** (required for free Streamlit Cloud tier)
4. Don't initialize with README (we already have files)

### Step 3: Push Your Code to GitHub

Open PowerShell/Terminal in your project folder and run:

```bash
# Navigate to your project folder
cd "d:\Desktop\Git\cassava_MobileNetv2"

# Initialize git repository (if not already)
git init

# Track the model file with Git LFS
git lfs track "*.keras"

# Add all files
git add .

# Commit
git commit -m "Initial commit: Cassava disease classifier with MobileNetV2"

# Add your GitHub repository as remote (replace with your repo URL)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**Important:** The model file `cassava_baseline_mobilenetv2.keras` will be uploaded via Git LFS, which handles large files properly.

### Step 4: Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click **"New app"**
3. Connect your GitHub account (if not already connected)
4. Select:
   - **Repository**: `YOUR_USERNAME/YOUR_REPO_NAME`
   - **Branch**: `main`
   - **Main file path**: `app.py`
5. Click **"Deploy!"**

### Step 5: Wait for Deployment

- Initial deployment takes 5-10 minutes
- Streamlit Cloud will install dependencies from `requirements.txt`
- You'll see build logs in real-time
- Once complete, your app will be live at: `https://YOUR_USERNAME-YOUR_REPO_NAME.streamlit.app`

## 📁 Repository Structure

```
cassava_MobileNetv2/
├── app.py                                  # Streamlit application
├── cassava_baseline_mobilenetv2.keras     # Trained model (Git LFS)
├── requirements.txt                        # Python dependencies
├── .gitattributes                         # Git LFS configuration
├── cassava_baseline.ipynb                 # Training notebook
└── README.md                              # This file
```

## 🔧 Files Explained

### `app.py`
The main Streamlit application with:
- Image upload interface
- Real-time prediction using the trained model
- Visual display of results with confidence scores
- Class probability breakdown

### `requirements.txt`
Python packages needed:
- `streamlit` - Web app framework
- `tensorflow` - Deep learning framework
- `numpy` - Numerical computing
- `Pillow` - Image processing

### `.gitattributes`
Configures Git LFS to handle large model files (`.keras`, `.h5`, `.pb`)

## 🐛 Troubleshooting

### Model File Too Large
If Git push fails due to file size:
```bash
# Ensure Git LFS is tracking the model
git lfs track "*.keras"
git add .gitattributes
git add cassava_baseline_mobilenetv2.keras
git commit -m "Track model with Git LFS"
git push
```

### App Crashes on Streamlit Cloud
Check the logs in Streamlit Cloud dashboard:
- Ensure all files are pushed to GitHub
- Verify `requirements.txt` has correct package versions
- Check that model file uploaded correctly via Git LFS

### TensorFlow Version Issues
If you get TensorFlow errors, you may need to adjust the version in `requirements.txt`:
```
tensorflow==2.15.0  # or tensorflow-cpu==2.15.0 for smaller size
```

### Out of Resources
Streamlit Cloud free tier has resource limits. If your app crashes:
- Consider using `tensorflow-cpu` instead of full `tensorflow`
- Optimize model loading with `@st.cache_resource`
- Reduce image preprocessing operations

## 🔄 Updating Your App

To update your deployed app:

```bash
# Make changes to app.py or other files
# Then commit and push
git add .
git commit -m "Description of changes"
git push
```

Streamlit Cloud automatically redeploys when you push to GitHub!

## 📊 Model Information

- **Architecture**: MobileNetV2 (pretrained on ImageNet)
- **Input Size**: 224x224 pixels RGB
- **Classes**: 
  - CBSD (Cassava Brown Streak Disease)
  - CMD (Cassava Mosaic Disease)
  - Healthy
- **Training Method**: Transfer learning with fine-tuning

## 🌐 Sharing Your App

Once deployed, share your app URL:
```
https://YOUR_USERNAME-YOUR_REPO_NAME.streamlit.app
```

Anyone can access it without installation!

## 💰 Costs

- **GitHub**: Free for public repositories
- **Streamlit Cloud**: Free tier includes:
  - 1 GB memory
  - 1 CPU core
  - Unlimited public apps
  - Community support

## 📚 Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [Streamlit Cloud Documentation](https://docs.streamlit.io/streamlit-community-cloud)
- [Git LFS Documentation](https://git-lfs.github.com/)
- [TensorFlow Documentation](https://www.tensorflow.org/api_docs)

## 📝 License

This project is for educational and research purposes.

## 👨‍💻 Support

If you encounter issues:
1. Check Streamlit Cloud logs
2. Review GitHub repository files
3. Consult [Streamlit Community Forum](https://discuss.streamlit.io)

---

**Happy Deploying! 🚀**
