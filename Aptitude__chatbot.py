from openai import OpenAI


client = OpenAI(
    api_key = "****",
    base_url = "****"

)
while True : 
    user_input = input("You: ")
    if user_input in ("Quit","quit","QUIT") :
        print("bot: GoodBye")
        break;
    response = client.chat.completions.create(
    model = "llama3-70b-8192",
    messages = [
       {"role":"system", "content" : "You are a Aptitude bot, provide information only related to Aptitude"},
       {"role" : "user", "content" : user_input}
    ]
    )
    print("Bot: ", response.choices[0].message.content)