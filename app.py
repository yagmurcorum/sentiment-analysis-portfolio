import streamlit as st
import requests
import time

# Page configuration
st.set_page_config(
    page_title="Sentiment Analysis AI",
    page_icon="",
    layout="wide"
)

# Custom styling with CSS
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    .stButton > button {
        background: linear-gradient(90deg, #ff6b6b, #ee5a24);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 12px 30px;
        font-weight: bold;
        font-size: 16px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }
    .stTextArea > div > div > textarea {
        background-color: rgba(255,255,255,0.1);
        border: 2px solid rgba(255,255,255,0.2);
        border-radius: 15px;
        color: #333333 !important;
        font-size: 16px;
    }
    .stTextArea > div > div > textarea::placeholder {
        color: rgba(255,255,255,0.7);
    }
    .success-box {
        background: linear-gradient(90deg, #00b894, #00a085);
        padding: 20px;
        border-radius: 15px;
        margin: 10px 0;
    }
    .error-box {
        background: linear-gradient(90deg, #e17055, #d63031);
        padding: 20px;
        border-radius: 15px;
        margin: 10px 0;
    }
    .warning-box {
        background: linear-gradient(90deg, #fdcb6e, #e17055);
        padding: 20px;
        border-radius: 15px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Main content – Two-column layout
col1, col2 = st.columns([2, 1])

with col1:
    st.title(" Sentiment Analysis AI")
    st.write("📝 Enter a sentence in English to predict its sentiment:")

    # Metin giriş alanı - session state ile
    text = st.text_area(
        "✍️ Your Text", 
        value=st.session_state.get('example_text', ''),
        placeholder="Type your sentence here...",
        height=150,
        key="text_input"
    )

    # Analyze button
    if st.button("🔍 Analyze Sentiment", type="primary"):
        if text.strip() == "":
            st.markdown('<div class="warning-box">⚠️ Please enter some text.</div>', unsafe_allow_html=True)
        else:
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/analyze",
                    json={"text": text}
                )
                
                if response.status_code == 200:
                    result = response.json()
                    
                    # Display results
                    sentiment = result['sentiment']
                    confidence = result['confidence']
                    
                    # Display sentiment with emoji
                    sentiment_emoji = {
                        'positive': '😊',
                        'negative': '😞', 
                        'neutral': '😐'
                    }.get(sentiment, '🤔')
                    
                    st.markdown(f'''
                    <div class="success-box">
                        <h3>{sentiment_emoji} Analysis Result</h3>
                        <p><strong>Sentiment:</strong> {sentiment.title()}</p>
                        <p><strong>Confidence:</strong> {confidence:.1%}</p>
                    </div>
                    ''', unsafe_allow_html=True)
                            
                else:
                    st.markdown('<div class="error-box">⚠️ Please enter a meaningful sentence (at least 3 characters).</div>', unsafe_allow_html=True)
                        
            except:
                st.markdown('<div class="error-box">⚠️ Connection error. Please check if API is running.</div>', unsafe_allow_html=True)

with col2:
    st.write("### 📋 Quick Examples")
    examples = [
        "I love this movie!",
        "This is terrible.",
        "The weather is okay today.",
        "Amazing experience!",
        "Very disappointing."
    ]
    
    for example in examples:
        if st.button(f"💡 {example[:20]}...", key=example):
            st.session_state.example_text = example
            st.rerun()
    
    st.write("---")
    st.write("### 🎯 Tips")
    st.write("• Use English sentences")
    st.write("• Be specific for better results")
    st.write("• Check confidence scores")
