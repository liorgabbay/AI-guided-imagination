from huggingface_hub import InferenceClient

token = "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"

example1 = """Find a comfortable place to sit or lie down. Close your eyes.

Take a few deep breaths to help you relax. Inhale deeply through your nose, hold for a moment, and then exhale slowly 
through your mouth. (PAUSE, 10 SEC)

Imagine a strong, secure container. This could be a safe, a vault, a box, or any container that feels secure to you. 
Picture it in detail—its size, shape, color, and material. (PAUSE, 15 SEC)

Think of a calm and peaceful memory from before your war experiences. Recall a specific day or moment when you felt 
at ease, such as spending time with family, enjoying a favorite hobby, or relaxing in nature. (PAUSE, 20 SEC)

Allow yourself to feel the peace and relaxation from this memory. Let it wash over you, creating a sense of calm and 
tranquility. (PAUSE, 20 SEC)

(see how we Slowly Addressing Feelings)
Gradually let your thoughts move towards the moments just before your intense experiences began. Think about the 
couple of minutes leading up to the event. What were you doing? Who were you with? How were you feeling? (PAUSE, 20 SEC)

Now, bring to mind the intense feelings from your war experiences. Visualize placing the thoughts, images, 
and emotions associated with these experiences into your container. This includes memories of combat, loss, 
and fear that contribute to your distress. (PAUSE, 30 SEC)

Carefully place each item related to these feelings into the container. As you do this, remind yourself that you are 
in control. You can decide when to open the container and address these items. For now, they are safely contained. (
PAUSE, 30 SEC)


Close the container securely. Lock it with a key, a code, or a combination. Feel the weight of the lock and know that 
your intense feelings are safely stored away, reducing the immediate impact. (PAUSE, 20 SEC)

Take a moment to appreciate the security of your container. Know that you can revisit it when you are ready, 
but for now, it is safely stored away. (PAUSE, 20 SEC)

(see how we Exiting from the Scene Slowly)

Now, gradually shift your focus back to your peaceful memory from earlier. Feel the calm and tranquility once again 
enveloping you. (PAUSE, 20 SEC)

As you let go of the intense feelings, imagine them securely locked away, and bring yourself back to the here and 
now. Take a deep breath, feeling grounded and safe. (PAUSE, 20 SEC)

When you feel ready, slowly bring your awareness back to the present moment. Take yourself out of the scene and back 
to where you are right now. (PAUSE, 10 SEC)

Count to 3, and open your eyes. (PAUSE, 5 SEC)

Notice how you feel right now. Allow yourself to carry this sense of control and security with you throughout your day."""

example2 = """Find a comfortable place to sit or lie down. Close your eyes.

Take a few deep breaths to help you relax. Inhale deeply through your nose, hold for a moment, and then exhale slowly 
through your mouth. (PAUSE, 10 SEC)


Imagine a beautiful garden where you feel completely safe and at peace. This garden is your sanctuary, filled with 
your favorite plants, flowers, and trees. (PAUSE, 15 SEC)


Walk through your garden and engage your senses. Feel the soft ground beneath your feet, smell the fragrant flowers, 
and listen to the gentle sounds of nature around you. (PAUSE, 20 SEC)

Allow yourself to feel completely at ease in this beautiful place. Let the tranquility of the garden wash over you, 
creating a deep sense of peace. (PAUSE, 20 SEC)

(see how we Slowly Addressing Feelings)

Think back to a good moment that happened before your intense experiences. Maybe you were sharing a laugh with a 
friend, receiving a letter from home, or experiencing a quiet, peaceful moment. Let this memory fill you with warmth. 
(PAUSE, 20 SEC)

As you continue to walk, allow yourself to think about how you felt as your war experiences were beginning. Notice 
any changes in your emotions or physical sensations. (PAUSE, 20 SEC)

In this healing spot, bring to mind the intense feelings from your war experiences. Visualize planting seeds that 
represent these feelings in the soil. These seeds symbolize your experiences, pain, and memories from the 
battlefield, loss, and fear that contribute to your distress. (PAUSE, 30 SEC)

As you plant these seeds, imagine the earth absorbing them, transforming the pain into growth and healing. See the 
seeds sprouting into beautiful plants, each representing a part of your healing journey. (PAUSE, 30 SEC)


Spend some time nurturing your garden. Water the plants, remove any weeds, and feel the healing energy flowing 
through you. Know that you are tending to these intense feelings and allowing them to transform into something 
positive, easing your distress. (PAUSE, 30 SEC)

(see how we Exiting from the Scene Slowly)

Now, shift your focus back to the peaceful elements of your garden. Notice the beauty around you and feel the 
calmness it brings. (PAUSE, 20 SEC)

Let go of the intense feelings, knowing they are being transformed in your garden, and bring yourself back to the 
here and now. Take a deep breath, feeling grounded and at peace. (PAUSE, 20 SEC)

When you feel ready, slowly bring your awareness back to the present moment. Take yourself out of the garden and back 
to where you are right now. (PAUSE, 10 SEC)

Count to 3, and open your eyes. (PAUSE, 5 SEC)

Notice how you feel right now. Allow yourself to carry this sense of healing and transformation with you throughout 
your day."""

example3 = """Find a comfortable place to sit or lie down. Close your eyes.

Take a few deep breaths to help you relax. Inhale deeply through your nose, hold for a moment, and then exhale slowly 
through your mouth. (PAUSE, 10 SEC)

Imagine a warm, healing light above you. This light can be any color that feels soothing and comforting. Picture it 
shining down on you, enveloping you in a gentle, healing glow. (PAUSE, 15 SEC)

Focus on the physical sensations in your body. Feel the warmth and weight of the light as it touches your skin, 
relaxing your muscles and calming your mind. (PAUSE, 20 SEC)

Allow yourself to feel completely at ease in this healing light. Let the tranquility and warmth of the light wash 
over you, creating a deep sense of peace. (PAUSE, 20 SEC)

(see how we Slowly Addressing Feelings)

Think of a specific positive moment before your intense experiences. Perhaps it was a quiet evening with friends, 
a moment of reflection, or a time when you felt safe and happy. Let this memory bring a smile to your face. (PAUSE, 
20 SEC)

Allow your thoughts to gently touch on the couple of minutes leading up to your intense experiences. What were you 
doing? How were you feeling? Notice the changes in your emotions and physical sensations. (PAUSE, 20 SEC)

As the light envelops you, bring to mind the intense feelings from your war experiences. Visualize the light focusing 
on the areas of your body and mind where you feel the pain and tension from these experiences. This includes 
flashbacks, anxiety, and hypervigilance associated with your distress. (PAUSE, 30 SEC)

Allow the light to penetrate these areas, dissolving the pain and tension. Feel the warmth and healing energy 
spreading through your body, replacing the darkness with light and peace. (PAUSE, 30 SEC)

As the light continues to heal you, imagine it transforming the intense memories and feelings. See these feelings 
being lifted away, carried by the light, and transformed into positive energy, helping to alleviate your distress. (
PAUSE, 30 SEC)

Feel a sense of relief and release as the light works its way through you, cleansing and healing every part of your 
being. (PAUSE, 30 SEC)

(see how we Exiting from the Scene Slowly)

Now, shift your focus back to the peaceful warmth of the light. Feel its soothing presence and let it bring you back 
to a state of calm. (PAUSE, 20 SEC)

Let go of the intense feelings, knowing they have been transformed, and bring yourself back to the here and now. Take 
a deep breath, feeling grounded and peaceful. (PAUSE, 20 SEC)


When you feel ready, slowly bring your awareness back to the present moment. Take yourself out of the light and back 
to where you are right now. (PAUSE, 10 SEC)

Count to 3, and open your eyes. (PAUSE, 5 SEC)

Notice how you feel right now. Allow yourself to carry this sense of healing and light with you throughout your day."""

guidelines = """Find a comfortable place to sit or lie down. Close your eyes.
    Take a few deep breaths to help you relax.
    Picture a setting that is calm and peaceful.
    This could be a beach, a mountain setting, a meadow, or a scene that you choose.
    
    Add some detail to your scene.. For example, is there a breeze? How does it feel? What do you smell? What does 
    the sky look like? Is it clear, or are there clouds? It often helps to add a path to your scene. For example, 
    as you enter the meadow, imagine a path leading you through the meadow to the trees on the other side. As you 
    follow the path farther into the meadow, you feel more and more relaxed. Take a few minutes to breathe slowly and 
    feel the calm. This is best done when you are deep into your scene and are feeling relaxed.
    
    Think of a "return" cue.
    Think of a simple word or sound that you can use in the future to help you return to this place.
    
    Exit from your scene. When you are ready, slowly take yourself out of the scene and back to the present. Tell 
    yourself that you will feel relaxed and refreshed and will bring your sense of calm with you.
    
    Count to 3, and open your eyes.
    Notice how you feel right now.
    
    
    few more guidelines : make it personal to the user and gently mention like in the following example, 
    the user situation and try to a toach it to good places in the imagination."""


def generate_response(prompt):
    client = InferenceClient("meta-llama/Meta-Llama-3-8B-Instruct", token=token)
    prompt = (
            "We are creating a guided imagery session for the user. Here are the guidelines on how to make a guided imagery session:" + guidelines +
            "And here is 3 examples that address the war trauma and PTSD (you need to use them for learning and "
            "combine the approach for the best result, but"
            "adjust it to the user trauma: example1" + example1 +
            "example2" + example2 + "example3" + example3 +
            "\nI would like you to create a guided imagery session tailored to the user's needs. For instance, "
            "addressing a problem such as PTSD trauma. Remember, our goal is to help the user feel more at ease, "
            "not to increase their stress, so please address the trauma slowly and after it exit from it slowly,  Now, "
            "with these instructions in mind, please begin immediately Speak"
            "directly to the user!, encouraging them to relax. Reassure them that if they ever feel uncomfortable "
            "during the session, they can pause and resume later. Use pauses (PAUSE, X SEC) to give the user time to "
            "do relation and breath and"
            "to absorb and reflect.and dont mention what you are doing, for example ( Addressing the user's trauma) "
            "also please start immediately the session and please dont write Here is a guided imagery "
            "session tailored to situation   Here is the user's situation and"
            "description please adjust the guided imagery to this,"
            
            "and address the issue during the session at list 4 times and as much you can but not to much, and build "
            "it slowly,dont address it immediately, build it:" + prompt)
    response = client.chat_completion(
        messages=[{"role": "user", "content": prompt}],
        max_tokens=5000,
        stream=False
    )
    return response.choices[0].message.content


def generate_response_without_few_shot(prompt):
    client = InferenceClient("meta-llama/Meta-Llama-3-8B-Instruct", token=token)
    prompt = (
            "create guided imagination for this user situation" + prompt)
    response = client.chat_completion(
        messages=[{"role": "user", "content": prompt}],
        max_tokens=5000,
        stream=False
    )
    return response.choices[0].message.content


