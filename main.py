import streamlit as st
import time



# Title of the app
st.title('SPECIAL NOTE FOR SPECIAL ONE ❤️')

font_css = '''
<style>
body {
    font-family: 'Arial', sans-serif;  /* Change the font family of the whole app */
}
.title {
    font-size: 20px;  /* Change the font size of the title */
    font-family: 'Comic Sans MS', cursive, sans-serif;  /* Change the font style of the title */
}
.wrap-text {
    white-space: pre-wrap;       /* CSS3 */
    white-space: -moz-pre-wrap;  /* Firefox */
    white-space: -pre-wrap;      /* Opera */
    white-space: -o-pre-wrap;    /* Opera */
    word-wrap: break-word;       /* IE */
    font-size: 16px;  /* Change the font size of the text */
    /*font-family: 'Courier New', Courier, monospace;   Change the font style of the text */
    font-style: oblique 23deg;
}

.foot{
    white-space: pre-wrap;       /* CSS3 */
    white-space: -moz-pre-wrap;  /* Firefox */
    white-space: -pre-wrap;      /* Opera */
    white-space: -o-pre-wrap;    /* Opera */
    word-wrap: break-word;       /* IE */
    font-size: 20px;
    font-style: oblique 23deg;
    }
</style>
'''

st.markdown(font_css, unsafe_allow_html=True)

# Display a button
if st.button('CLICK HERE SUNSHINE THIS IS SOMETHING FOR YOU!!'):
    placeholder1 = st.empty()  # Create an empty placeholder
    message1 = '''
        Can’t pinpoint the exact moment I fell for you, but what I know for certain is that “YOU BELONG TO ME” Yes, YOU ARE MINE and I proudly admit I chose you to tease and irritate for the rest of my life. The world doesn’t matter to me as long as I HAVE YOU, because I know you’ll never leave me, no matter what. You are extraordinary, your vibes are unique and I feel whole when I am with you.I want to spend the rest of my life with you, teasing you, irritating you and yes troubling you a bit too(IYKYK).But I promise, my LOVE for you will always be UNMATCHED . 
STAY MINE FOREVER 
I LOVE YOU SUNSHINE ❤️ '''

    message2 = '''SUNSHINE, YOU ARE MY EVERYTHING, AND I LOVE YOU MORE THAN WORDS CAN EVER EXPRESS.'''
    typed_message = ''
    # max_chars = st.slider('Adjust text length', min_value=1, max_value=len(message1 + message2),
    #                       value=len(message1 + message2))

    # Typing effect
    for char in message1:
        typed_message += char
        placeholder1.markdown(f'<div class="wrap-text">{typed_message}</div>',
                             unsafe_allow_html=True)  # Update the placeholder text with wrapping
        # placeholder.text(typed_message)  # Update the placeholder text
        time.sleep(0.05)
    placeholder2 = st.empty()
    typed_message1= '\n\n'
    for char in message2:
        typed_message1 += char
        placeholder2.markdown(f'<div class="foot">{typed_message1}</div>',
                             unsafe_allow_html=True)  # Update the placeholder text with wrapping
        # placeholder.text(typed_message)  # Update the placeholder text
        time.sleep(0.05)
