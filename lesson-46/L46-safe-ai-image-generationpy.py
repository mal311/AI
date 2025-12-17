import streamlit as st
import re
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

# Initialize Gemini API client
client = genai.Client(api_key="AIzaSyBDt6FHhJjOTFQtdmtz7hseDnUiSYgiUSM") 

def is_prompt_safe(prompt: str) -> bool:
    """
    Basic filter to avoid generating harmful or restricted content.
    Extend this list based on your organization's content policy.
    """

    forbidden_keywords = [
        "violence", "weapon", "gun", "blood", "nude", "porn", "drugs", "hate", "racism", "sex",
        "terror", "bomb", "abuse", "kill", "death", "suicide", "self-harm", "hate speech"
    ]

    pattern = re.compile("|".join(forbidden_keywords), re.IGNORECASE)

    return not bool(pattern.search(prompt)) 

def generate_image(prompt: str):
    """
    Generate an image using Gemini API with the given prompt.
    Returns image data or error message.
    """

    if not is_prompt_safe(prompt):
        return None, "⚠️ Your prompt contains restricted or unsafe content. Please modify and try again"    

    try:
        # Use the correct model name and API structure based on reference
        model = "gemini-2.0-flash-preview-image-generation"

        contents = [
            types.Content(
                role="user",
                parts=[
                    types.Part.from_text(text=prompt),
                ],
            ),
        ]
 
        generate_content_config = types.GenerateContentConfig(
            response_modalities=[
                "IMAGE",
                "TEXT",
            ],
            response_mime_type="text/plain",
        )        

        # Use streaming approach like in the reference
        for chunk in client.models.generate_content_stream(
            model=model,
            contents=contents,
            config=generate_content_config,
        ):
            if (
                chunk.candidates is None
                or chunk.candidates[0].content is None
                or chunk.candidates[0].content.parts is None
            ):
                continue                

            # Check for image data
            if (chunk.candidates[0].content.parts[0].inline_data and chunk.candidates[0].content.parts[0].inline_data.data):
                inline_data = chunk.candidates[0].content.parts[0].inline_data
                
                data_buffer = inline_data.data
                
                # Convert to PIL Image
                image = Image.open(BytesIO(data_buffer))
                return image, None           

            # Handle text response
            elif chunk.text:
                # Continue to next chunk - text might come before image
                continue        

        return None, "No image was generated in the response."        

    except Exception as e:
        return None, f"Error during image generation: {str(e)}"
    
def main():
    st.set_page_config(page_title="Safe AI Image Generator", layout="centered")

    st.title("???? Safe AI Image Generator")

    st.write(
        "Enter a description to generate a safe and responsible AI image using Gemini 2.0 Flash. "

        "Examples: 'A serene sunset over a mountain lake', 'A futuristic city skyline at night'"
    )    

    # Add info about the model
    st.info("This app uses Gemini 2.0 Flash Preview for image generation with streaming response.")    

    with st.form(key="image_gen_form"):
        prompt = st.text_area(
            "Image Description:",
            height=120,
            placeholder="Describe the image you want to generate... Be specific for better results!"
        )

        submit = st.form_submit_button("Generate Image")        

        if submit:
            if not prompt.strip():
                st.warning("⚠️ Please enter an image description.")

            else:
                with st.spinner("Generating image... This may take a few moments."):
                    image, error = generate_image(prompt.strip())
                    
                if error:
                    st.error(error)

                elif image:
                    st.image(image, caption="Generated Image", use_container_width=True)

                    # Store image in session state for download outside form
                    st.session_state.generated_image = image
                    
                else:
                    st.error("Failed to generate image. Please try again with a different prompt.")
                    
    # Download button outside the form
    if hasattr(st.session_state, 'generated_image') and st.session_state.generated_image:
        buf = BytesIO()

        st.session_state.generated_image.save(buf, format='PNG')

        byte_im = buf.getvalue()

        st.download_button(
            label="???? Download Generated Image",
            data=byte_im,
            file_name="ai_generated_image.png",
            mime="image/png",
            help="Click to download the generated image"
        ) 

if __name__ == "__main__":
    main()
    # to run this streamlit web app, write python -m streamlit run filename.py in the terminal