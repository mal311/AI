import streamlit as st
from google import genai
from google.genai import types
import io

#Initialize the Gemini API client
client = genai.Client(api_key="AIzaSyDu0-jCuQ0OamtxxDxCR1bzEcqx1NUofU0")

def generate_response(prompt: str, temperature: float = 0.3) -> str:
    """Generate a response from Gemini API"""
    try:
        contents = [types.Content(role="user", parts=[types.Part.from_text(text=prompt)])]
        config_params= types.GenerateContentConfig(temperature=temperature)
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=contents, config=config_params)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def setup_ui():
    st.set_page_config(page_title="AI Teaching Assistant", layout="centered")
    st.title("🤖 AI Teaching Assistant")
    st.write("Ask me anything about various subjects, and I'll provide an answer.")

    if "history" not in st.session_state:
        st.session_state.history=[]
    
    #Buttons in a horizontal layout: Clear and Export
    col_clear, col_export = st.columns([1,2])
    with col_clear:
        if st.button(" 🧹 Clear conversation"):
            st.session_state.history = []
        #st.experimental_rerun()
    with col_export:
        if st.session_state.history:
            #Prepare converstaion text for export
            export_text = ""
            for idx, qa in enumerate(st.session_state.history, start=1):
                export_text += f"Q{idx}: {qa['question']}\n"
                export_text += f"A{idx}: {qa['answe']}\n\n"
            
            bio = io.BytesIO()
            bio.write(export_text.encode("utf-8"))
            bio.seek(0)

            st.download_button(
                label=" 📥Export Chat History",
                data=bio,
                file_name="AI_Teaching_Assistant_Conversation.txt",
                mime="text/plain"
            )
    
    #User input
    user_input = st.text_input("Enter your question here:")

    if st.button("Ask"):
        if user_input.strip():
            with st.spinner("Generating AI Response..."):
                response = generate_response(user_input.strip())
            st.session_state.history.append({"question": user_input.strip(), "answer": response})
        else:
            st.warning("⚠️ Please enter a question before clicking Ask.")
    
    #Display conversation history in scrollabe container
    st.markdown("###Conversation history")
    st.markdown(
        """
        <style>
        .history-box {
            max-height:400px;
            overflow-y: auto;
            border: 1px solid #ddd;
            padding: 12px;
            background-color: #f9f9f9;
            border-radius: 6px;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-erif;
        }

        .question{
            font-weight: 600;
            color: #0a6ebd;
            margin-top: 12px; 
            margin-bottom: 4px;
        }
        .answer {
            margin-bottom:16px;
            white-space: pre-wrap;
            color: #333;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    history_html = '<div class="history-box">'
    for idx, qa in enumerate(st.session_state.history, start=1):
        q = qa["question"]
        a = qa["answer"]
        history_html += f'<div class="question">Q{idx}: {q}</div>'
        history_html += f'<div class="answee">A{idx}: {a}</div>'
    history_html += '</div>'
    st.markdown(history_html, unsafe_allow_html=True)

def main():
    setup_ui()

if __name__ =="__main__":
    main()
    #To run this streamlit web app, write python -m streamlit run filename.py in the terminal