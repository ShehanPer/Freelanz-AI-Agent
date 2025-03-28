from openai import OpenAI
from firebase import simplify_bot_responses

client = OpenAI(
  base_url="https://integrate.api.nvidia.com/v1",
  api_key="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"  # Ensure this is the correct API key
)
def get_response(messages, history, client_name):
    #formatted_history = simplify_bot_responses(history)
    print(f"Formatted history: {history}")  # Debugging statement
    current_chat = []
    
    template = [
        {"role": "system", "content": "You are a freelancing assistant chatbot. Your task is to answer the user's questions based on past conversations and provide the best possible answer to help users to handle their clients. user name != client name, user name is the name of the user who is using the chatbot. client name is the name of the client who belongs to user's bussiness."},
        {"role": "system", "content": f"Client name: {client_name}. The past messages include previous interactions. past messages={history}, current messages={current_chat}"}
    ] + messages  # Ensure messages is a list

    try:
        completion = client.chat.completions.create(
            model="meta/llama-3.1-70b-instruct",
            messages=template,  
            temperature=0.2,
            top_p=0.7,
            max_tokens=1024,
            stream=True
        )

        response = ""
        for chunk in completion:
            if chunk.choices[0].delta.content is not None:
                response += chunk.choices[0].delta.content
        print(f"Bot response: {template}")  # Debugging statement

        current_chat.append({"role": f"{client_name}", "content": messages})
        current_chat.append({"role": "assistant", "content": response})
        return response

    except Exception as e:
        return f"Error: {str(e)}"
