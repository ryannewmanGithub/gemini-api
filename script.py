from google import genai
import sys
import time

FILENAME = "hiddenfile.txt"

with open(FILENAME, 'r') as f:
    the_api_key = f.readline().strip()

client = genai.Client(api_key=the_api_key)

while True:

    userinput = input("Ask Gemini: ")

    if userinput == "exit":
        sys.exit(0)
        
    print("Thinking...")

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=userinput,
    )

    #print(response.text)

    txt = response.text
    word_list = txt.split(" ")
    
    last = len(word_list)

    for i in range(last):
        word = word_list[i]
        if i != last - 1:
            print(word, end=' ')
        else:
            print(word, end='')
        
        time.sleep(0.0004)
    

    