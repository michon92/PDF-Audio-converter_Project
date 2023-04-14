import pyttsx3
import PyPDF2


with open('auto_swiat_fso.pdf', 'rb') as book:
    reader = PyPDF2.PdfReader(book)
    audio_reader = pyttsx3.init()
    voice = audio_reader.getProperty('voices')
    audio_reader.setProperty('voice', voice[0].id)
    audio_reader.setProperty("rate", 150)

    for page in range(len(reader.pages)):
        next_page = reader.pages[page]
        content = next_page.extract_text()
        audio_reader.say(content)
        audio_reader.runAndWait()
