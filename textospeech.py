# 3️⃣ Initalize a pipeline
from kokoro import KPipeline
import sounddevice as sd  

# 🇨🇳 'z' => Mandarin Chinese: pip install misaki[zh]
pipeline = KPipeline(lang_code='a')  # Ensure lang_code matches voice

# Text to speak
text = '''
🤖 Artificial intelligence is evolving at a breakneck speed, bringing with it models tailored for various tasks. 
Among OpenAI's recent innovations, GPT-4o and GPT-o1 stand out as transformative tools in their own right. While both leverage advanced AI frameworks, 
their differences are stark, making each better suited for distinct applications. In this article, we’ll explore how these two models differ in speed, 
reasoning, functionality, and potential use cases, giving you a clear roadmap to choose the right one for your needs.'''

# 4️⃣ Generate and play audio in a loop
generator = pipeline(
    text, voice='af_sarah',  # Change voice here
    speed=1, split_pattern=r'\n+'
)

# VOICE_NAME = [
#     'af_bella',   # American English - Bella
#     'af_sarah',   # American English - Sarah
#     'am_adam',    # American Male - Adam
#     'am_michael', # American Male - Michael
#     'bf_emma',    # British Female - Emma
#     'bf_isabella',# British Female - Isabella
#     'bm_george',  # British Male - George
#     'bm_lewis',   # British Male - Lewis
#     'af_nicole',  # American English - Nicole
#     'af_sky'      # American English - Sky
# ]

# Play each generated audio clip
for i, (gs, ps, audio) in enumerate(generator):
    print(i)  # Index
    print(gs) # Graphemes/text
    print(ps) # Phonemes

    # Play audio using sounddevice
    sample_rate = 22050  # Higher quality sample rate
    sd.play(audio, samplerate=sample_rate)
    sd.wait()  # Wait until audio finishes playing
    #sf.write(f'{i}.wav', audio, sample_rate) # Uncomment to save audio files
