import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import io

# Page configuration
st.set_page_config(
    page_title="Cassava Disease Classifier",
    page_icon="🌿",
    layout="centered"
)

# Cache the model to avoid reloading
@st.cache_resource
def load_model():
    """Load the trained MobileNetV2 model"""
    try:
        model = tf.keras.models.load_model('cassava_baseline_mobilenetv2.keras')
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

# Class names
CLASS_NAMES = ['CBSD (Cassava Brown Streak Disease)', 
               'CMD (Cassava Mosaic Disease)', 
               'Healthy']

# Define colors for each class
CLASS_COLORS = {
    'CBSD (Cassava Brown Streak Disease)': '#ff6b6b',
    'CMD (Cassava Mosaic Disease)': '#ffa500',
    'Healthy': '#51cf66'
}

def preprocess_image(image):
    """Preprocess the uploaded image for model prediction"""
    # Convert to RGB if necessary
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    # Resize to model's expected input size
    img = image.resize((224, 224))
    
    # Convert to numpy array
    img_array = np.array(img)
    
    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)
    
    return img_array

def predict(model, image):
    """Make prediction on the preprocessed image"""
    img_array = preprocess_image(image)
    predictions = model.predict(img_array, verbose=0)
    predicted_class_idx = np.argmax(predictions[0])
    confidence = predictions[0][predicted_class_idx]
    
    return CLASS_NAMES[predicted_class_idx], confidence, predictions[0]

# Main app
def main():
    # Title and description
    st.title("🌿 Cassava Disease Classifier")
    st.markdown("""
    This application uses a **MobileNetV2** deep learning model to classify cassava leaf diseases.
    
    Upload an image of a cassava leaf to detect:
    - **CBSD**: Cassava Brown Streak Disease
    - **CMD**: Cassava Mosaic Disease  
    - **Healthy**: No disease detected
    """)
    
    # Load model
    model = load_model()
    
    if model is None:
        st.error("Failed to load the model. Please ensure 'cassava_baseline_mobilenetv2.keras' is in the app directory.")
        return
    
    st.success("✅ Model loaded successfully!")
    
    # File uploader
    st.markdown("---")
    uploaded_file = st.file_uploader(
        "Choose a cassava leaf image...",
        type=['jpg', 'jpeg', 'png'],
        help="Upload a clear image of a cassava leaf"
    )
    
    if uploaded_file is not None:
        # Display uploaded image
        image = Image.open(uploaded_file)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Uploaded Image")
            st.image(image, use_container_width=True)
        
        with col2:
            st.subheader("Prediction")
            
            # Make prediction
            with st.spinner("Analyzing image..."):
                predicted_class, confidence, all_predictions = predict(model, image)
            
            # Display result with colored box
            result_color = CLASS_COLORS[predicted_class]
            
            st.markdown(f"""
            <div style="padding: 20px; border-radius: 10px; background-color: {result_color}20; border: 2px solid {result_color};">
                <h3 style="color: {result_color}; margin: 0;">{predicted_class}</h3>
                <p style="font-size: 24px; margin: 10px 0;"><strong>{confidence * 100:.2f}%</strong> confidence</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Show all class probabilities
            st.markdown("### Class Probabilities")
            for i, class_name in enumerate(CLASS_NAMES):
                prob = all_predictions[i] * 100
                st.progress(float(prob / 100))
                st.text(f"{class_name}: {prob:.2f}%")
        
        # Additional information
        st.markdown("---")
        st.markdown("""
        ### 📊 About the Model
        - **Architecture**: MobileNetV2 (pretrained on ImageNet)
        - **Input Size**: 224x224 pixels
        - **Classes**: 3 (CBSD, CMD, Healthy)
        - **Training**: Transfer learning with fine-tuning
        """)
    
    else:
        # Show sample instructions
        st.info("👆 Please upload a cassava leaf image to get started")
        
        st.markdown("---")
        st.markdown("""
        ### 💡 Tips for Best Results
        - Use clear, well-lit images
        - Ensure the leaf is clearly visible
        - Avoid blurry or very dark images
        - Images should show the leaf symptoms clearly
        """)

if __name__ == "__main__":
    main()
