import pyttsx3
import PyPDF2


with open('auto_swiat_fso.pdf', 'rb') as book:
    full_text = ''
    reader = PyPDF2.PdfReader(book)
    audio_reader = pyttsx3.init()
    voice = audio_reader.getProperty('voices')
    audio_reader.setProperty('voice', voice[1].id)
    audio_reader.setProperty("rate", 150)

    for page in range(len(reader.pages)):
        next_page = reader.pages[page]
        content = next_page.extract_text()
        full_text += content

    audio_reader.save_to_file(full_text, "myaudiobook2.mp3")
    audio_reader.runAndWait()
