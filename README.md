# AI Guided Imagery

This project is an AI platform for creating guided imagery using the Meta-Llama-3-8B-Instruct model.

Model Link: [Meta-Llama-3-8B-Instruct on Hugging Face](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct)

## Project Overview

The platform utilizes the Meta-Llama-3-8B-Instruct model to generate personalized guided imagery. By using few-shot learning, the model is adapted to respond accurately and create precise guided imagery sessions. These sessions include pauses for breathing and are tailored to the user's specific situations.

## How It Works

1. **User Interaction:** 
   - The user visits the website and inputs their current life situation to generate a guided imagery session.

2. **Model Processing:**
   - The model receives the prompt along with instructions and examples on how to perform the guided imagery.

3. **Text to Speech:**
   - We use Google's Text-to-Speech API to convert the model's text output into speech.

4. **Adding Background Sounds:**
   - Background sounds are added to create a pleasant atmosphere for the user.

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/liorgabbay/AI-guided-imagination.git
    cd ai-guided-imagery
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    python app.py
    ```


