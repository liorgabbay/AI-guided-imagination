from huggingface_hub import InferenceClient

token = "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"

example = """there is a Guided Imagery for PTSD learn from it: 

        Find a comfortable place to sit or lie down. Close your eyes. (PAUSE, 5 SEC)

        Take a few deep breaths to help you relax. Inhale deeply through your nose, hold for a moment, and then exhale slowly through your mouth. (PAUSE, 10 SEC)
        
        Picture yourself in a serene and peaceful place. This could be a beach with soft waves lapping at the shore, a quiet forest with sunlight filtering through the trees, or a calm meadow filled with wildflowers. Choose a place where you feel completely safe and at ease. (PAUSE, 15 SEC)
        
        As you settle into this place, take in the details around you. Notice the colors, the sounds, the scents. Feel the ground beneath you, whether it's warm sand, soft grass, or cool earth. (PAUSE, 20 SEC)
                
        Imagine a gentle breeze brushing against your skin. Feel the warmth of the sun or the coolness of the shade. Breathe in the fresh air and let it fill your lungs, bringing a sense of calm and relaxation. (PAUSE, 20 SEC)
        
        Now, envision a path appearing before you. This path leads you deeper into your safe place. As you begin to walk along this path, feel each step grounding you and connecting you to this peaceful environment. (PAUSE, 20 SEC)
        
        Find a spot in this safe place where you feel most at peace. This could be a cozy nook, a sunny patch of grass, or a favorite tree. Sit down in this spot and take a moment to absorb the tranquility. (PAUSE, 20 SEC)
        
        ( here we Addressing Trauma Gently -  we need address the what the user gave you, I will give you it later, but gently, here is how we addressed a PTSD trauma, if you have specific detailes in the user message you can mention it gently.)
                
        In this safe and serene place, allow yourself to bring to mind the situation that has been troubling you. Remember that you are in control and can choose to explore this at your own pace. Imagine a comforting presence with you, perhaps a wise and compassionate guide or your own higher self. This presence is here to support you, to listen, and to help you process your feelings. (PAUSE, 30 SEC)
        
        If any emotions arise, acknowledge them without judgment. It’s okay to feel what you’re feeling. You are safe, and you are not alone. Allow these feelings to exist in this safe place where they cannot harm you. (PAUSE, 30 SEC)
                
        Imagine a healing light shining down on you. This light can be any color that feels soothing to you. As it touches your head, let it clear away any dark thoughts. Allow the light to fill your mind with peace and clarity. (PAUSE, 30 SEC)
        
        Let the light move down to your heart, dissolving any heavy feelings and filling you with love and compassion. Allow the light to fill every part of your body, bringing a sense of relaxation and well-being. (PAUSE, 30 SEC)
                
        When you feel ready, think of a return cue. This could be a word, a sound, or an image that will help you return to this place of peace and safety whenever you need it. (PAUSE, 10 SEC)
        
        Slowly bring your awareness back to the present moment. Take yourself out of the scene and back to where you are right now. (PAUSE, 10 SEC)
        
        Tell yourself that you will bring the sense of calm and safety with you as you return. You are relaxed, refreshed, and supported. (PAUSE, 10 SEC)
        
        Count to 3, and open your eyes. (PAUSE, 5 SEC)
        
        Notice how you feel right now. Allow yourself to carry this sense of peace with you throughout your day."""

guidelines = """Find a comfortable place to sit or lie down. Close your eyes.
    Take a few deep breaths to help you relax.
    Picture a setting that is calm and peaceful.
    This could be a beach, a mountain setting, a meadow, or a scene that you choose.
    
    Add some detail to your scene..
    For example, is there a breeze? How does it feel? What do you smell? What does the sky look like? Is it clear, or are there clouds?
    It often helps to add a path to your scene. For example, as you enter the meadow, imagine a path leading you through the meadow to the trees on the other side. As you follow the path farther into the meadow, you feel more and more relaxed.
    Take a few minutes to breathe slowly and feel the calm.
    This is best done when you are deep into your scene and are feeling relaxed.
    
    Think of a "return" cue.
    Think of a simple word or sound that you can use in the future to help you return to this place.
    
    Exit from your scene.
    When you are ready, slowly take yourself out of the scene and back to the present. Tell yourself that you will feel relaxed and refreshed and will bring your sense of calm with you.
    
    Count to 3, and open your eyes.
    Notice how you feel right now.
    
    
    few more guidelines : make it personal to the user and gently mention like in the following example, the user situation and try to a toach it to good places in the imagination.  
    """



def generate_response(prompt):
    client = InferenceClient("meta-llama/Meta-Llama-3-8B-Instruct", token=token)
    prompt = ("We are creating a guided imagery session for the user. Here are the guidelines on how to make a guided imagery session:" +guidelines+
                "And here is an example:" + example +
                "I would like you to create a guided imagery session tailored to the user's needs. For instance, "
                "addressing a problem such as PTSD trauma. Remember, our goal is to help the user feel more at ease, "
                "not to increase their stress. Now, with these instructions in mind, please begin immediately. Speak "
                "directly to the user, encouraging them to relax. Reassure them that if they ever feel uncomfortable "
                "during the session, they can pause and resume later. Use pauses (PAUSE, X SEC) to give the user time to do relaxion and breath and "
                "to absorb and reflect. Here is the user's situation and description:" + prompt)
    response = client.chat_completion(
        messages=[{"role": "user", "content": prompt}],
        max_tokens=5000,
        stream=False
    )
    return response.choices[0].message.content
