import streamlit as st
import re
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

# Initialize Gemini API client
client = genai.Client(api_key="AIzaSyBDt6FHhJjOTFQtdmtz7hseDnUiSYgiUSM")

#AI teaching assistant
def run_ai_teaching_assistant():
    st.title("🤖 AI Teaching Assistant")
    st.write("Ask me anything about various subjects, and I'll provide an answer.")

    if "history_ata" not in st.session_state:
        st.session_state.history_ata=[]
    
    #Buttons: Clear and Export
    col_clear, col_export = st.columns([1,2])
    with col_clear:
        if st.button(" 🧹 Clear conversation", key="clear_ata"):
            st.session_state.history_ata = []

    with col_export:
        if st.session_state.history_ata:
            #Prepare converstaion text for export
            export_text = ""
            for idx, qa in enumerate(st.session_state.history_ata, start=1):
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
    

    user_input = st.text_input("Enter your question here:", key="input_ata")

    if st.button("Ask", key="ask_ata"):
        if user_input.strip():
            with st.spinner("Generating AI Response..."):
                response = generate_response(user_input.strip(), temperature=0.3)
            st.session_state.history_ata.append({"question": user_input.strip(), "answer": response})
        else:
            st.warning("⚠️ Please enter a question before clicking Ask.")
    
    #Display conversation history in scrollabe container
    st.markdown("###Conversation history")
    for idx, qa in enumerate(st.session_state.history_ata, start=1):
        st.markdown(f"**Q{idx}:** {qa['question']}")
        st.markdown(f"**A{idx}:** {qa['answer']}")
# Maths Mastermind
def run_Math_Mastermind():
    st.title("🧮 Math Mastermind")

    st.write("**Your Expert Mathematical Problem Solver** - From basic arithmetic to advanced calculus, I'll solve any math problem with detailed step-by-step explanations!")
    

    if "history_mm" not in st.session_state:
        st.session_state.history_mm = []
    if "input key_mm" not in st.session_state:
        st.session_state.input_key_mm = 0

    col_clear, col_export = st.columns([1, 2])

    with col_clear:
        if st.button("🧹 Clear Conversation", key="clear_mm"):
            st.session_state.history_mm = []
            st.experimental_rerun()

    with col_export:
        if st.session_state.history_mm:
            export_text = ""
            for idx, qa in enumerate(st.session_state.history, start=1):
                export_text += f"Q{idx}: {qa['question']}\n"
                export_text += f"A{idx}: {qa['answer']}\n\n"

            bio = io.BytesIO()
            bio.write(export_text.encode("utf-8"))
            bio.seek(0)

            st.download_button(
                label="📥 Export Math Solutions",
                data=bio,
                file_name="Math_Mastermind_Solutions.txt",
                mime="text/plain",
            )

    # Input and submit form
    with st.form(key="math_form", clear_on_submit=True):
        user_input = st.text_area(
            "🔢 Enter your math problem here:", 
            height=100,
            placeholder="Example: Solve x² + 5x + 6 = 0 or Find the integral of 2x + 3",
            key=f"user_input_{st.session_state.input_key}"
        )
        
        col1, col2 = st.columns([3, 1])
        with col1:
            submitted = st.form_submit_button("🧮 Solve Problem", use_container_width=True)

        with col2:
            difficulty = st.selectbox("Level", ["Basic", "Intermediate", "Advanced"], index=1)
        
        if submitted and user_input.strip():
            # Add difficulty context to the prompt
            enhanced_prompt = f"[{difficulty} Level] {user_input.strip()}"
            
            with st.spinner("🔍 Analyzing and solving your math problem..."):
                response = generate_response(enhanced_prompt)
            
            # Insert new Q&A at front (latest on top)
            st.session_state.history.insert(0, {
                "question": user_input.strip(), 
                "answer": response,
                "difficulty": difficulty
            })
            
            # Increment input key to reset the input field
            st.session_state.input_key += 1
            st.rerun()
        
        elif submitted and not user_input.strip():
            st.warning("⚠️ Please enter a math problem before clicking Solve Problem.")

    # Show conversation history
    if st.session_state.history:
        st.markdown("### 📋 Solution History (Latest First)")
        st.markdown(
            """
            <style>
            .history-box {
                max-height: 500px;
                overflow-y: auto;
                border: 2px solid #4CAF50;
                padding: 15px;
                background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
                border-radius: 10px;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            .question {
                font-weight: 700;
                color: #2E7D32;
                margin-top: 15px;
                margin-bottom: 8px;
                font-size: 16px;
            }
            .difficulty {
                display: inline-block;
                background-color: #FF9800;
                color: white;
                padding: 2px 8px;
                border-radius: 12px;
                font-size: 12px;
                font-weight: bold;
                margin-left: 10px;
            }
            .answer {
                margin-bottom: 20px;
                white-space: pre-wrap;
                color: #1B5E20;
                line-height: 1.6;
                background-color: rgba(255, 255, 255, 0.7);
                padding: 12px;
                border-radius: 8px;
                border-left: 4px solid #4CAF50;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

        history_html = '<div class="history-box">'
        total_questions = len(st.session_state.history)
        for idx, qa in enumerate(st.session_state.history):
            # Latest question gets the highest number (Q3, Q2, Q1...)
            question_num = total_questions - idx
            
            difficulty_badge = f'<span class="difficulty">{qa.get("difficulty", "N/A")}</span>' if "difficulty" in qa else ""
            
            history_html += f'<div class="question">Problem {question_num}: {qa["question"]}{difficulty_badge}</div>'

            history_html += f'<div class="answer">Solution {question_num}: {qa["answer"]}</div>'

        history_html += '</div>'
        st.markdown(history_html, unsafe_allow_html=True)
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    history_html = '<div class="history-box">'
    for idx, qa in enumerate(st.session_state.history, start=1):
        q = qa["question"]
        a = qa["answer"]
        history_html += f'<div class="question">Q{idx}: {q}</div>'
        history_html += f'<div class="answee">A{idx}: {a}</div>'
    history_html += '</div>'
    st.markdown(history_html, unsafe_allow_html=True)
