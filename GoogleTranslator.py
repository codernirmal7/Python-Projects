from googletrans import Translator

translator = Translator()

dest_lang_list = [
    "'en' for english",
    "'np' for nepali",
    "'hi' for hindi",
    "'fr' for french",
    "'es' for spanish"

]

print(dest_lang_list)
text = input("Enter the text you want to translate > ")
dest_lang = input("Enter the langauge code you want to transalte to (e.g , 'hi' for hindi , 'fr' for french)")

translated = translator.translate(text , dest=dest_lang)
print(f"Translated Text : {translated}")
