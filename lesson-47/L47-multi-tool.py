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

    with st.form(key="math_form", clear_on_submit=True):
        user_input = st.text_area(
            "🔢 Enter your math problem here:", 
            height=100,
            placeholder="Example: Solve x² + 5x + 6 = 0 or Find the integral of 2x + 3",
            key=f"user_input_{st.session_state.input_key_mm}"
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
                response = generate_math_response(enhanced_prompt)
            st.session_state.history_mm.insert(0, {
                "question": user_input.strip(), 
                "answer": response,
                "difficulty": difficulty
            })
            st.session_state.input_key_mm += 1
            st.rerun()
        elif submitted and not user_input.strip():
            st.warning("⚠️ Please enter a math problem before clicking Solve Problem.")

    if st.session_state.history_mm:
        st.markdown("### 📋 Solution History (Latest First)")
        for idx, qa in enumerate(st.session_state.history_mm):
            question_num=len(st.session_state.history_mm)-idx
            difficulty_badge= f"[{qa.get('difficulty', 'N/A')}]"
            st.markdown(f"**Problem {question_num} {difficulty_badge}:** {qa['question']}")
            st.markdown(f"**Solution {question_num}: **\n{qa['answer']}")

# -------- Safe AI Image Generator --------

def run_safe_ai_image_generator():
    st.title("🎨 Safe AI Image Generator")
    st.write("Enter a description to generate a safe and responsible AI image using Gemini 2.0 Flash.")

    def is_prompt_safe(prompt: str) -> bool:
        forbidden_keywords = [
            "violence", "weapon", "gun", "blood", "nude", "porn", "drugs", "hate", "racism", "sex",
            "terror", "bomb", "abuse", "kill", "death", "suicide", "self-harm", "hate speech"
        ]

        pattern = re.compile("|".join(forbidden_keywords), re.IGNORECASE)
        return not bool(pattern.search(prompt)) 

    def generate_image(prompt: str):
        if not is_prompt_safe(prompt):
            return None, "⚠️ Your prompt contains restricted or unsafe content. Please modify and try again"    
        try:
            model = "gemini-2.0-flash-preview-image-generation"
            contents = [types.Content(role="user", parts=[types.Part.from_text(text=prompt)])]
            config_params = types.GenerateContentConfig(
                response_modalities=["IMAGE", "TEXT"],
                response_mime_type="text/plain",
            )        

            # Use streaming approach like in the reference
            for chunk in client.models.generate_content_stream(
                model=model,
                contents=contents,
                config=config_params,
            ):
                if (
                    chunk.candidates is None
                    or chunk.candidates[0].content is None
                    or chunk.candidates[0].content.parts is None):
                    continue                
                if (chunk.candidates[0].content.parts[0].inline_data and 
                    chunk.candidates[0].content.parts[0].inline_data.data):
                    inline_data = chunk.candidates[0].content.parts[0].inline_data
                    data_buffer = inline_data.data
                    image = Image.open(BytesIO(data_buffer))
                    return image, None           
                elif chunk.text:
                    continue        
            return None, "No image was generated in the response."        
        except Exception as e:
            return None, f"Error during image generation: {str(e)}"
    
    with st.form(key="image_gen_form")