from dotenv import load_dotenv
import openai
import os

# 환경 변수 로드
load_dotenv()
conversation_history = []

def trim_conversation_history(history, max_tokens=4096):
    total_tokens = sum(len(message["content"].split()) for message in history)
    while total_tokens > max_tokens:
        removed_message = history.pop(0)
        total_tokens -= len(removed_message["content"].split())
    return history

def create_openai_client():
    return openai.OpenAI(api_key=os.getenv('API_KEY'))

def generate_answer(client, user_input):
    global conversation_history
    pre_prompt = "한국어로 친절하게 대답해줘 :)\n\n"
    full_prompt = f"{pre_prompt}{user_input}"
    
    conversation_history.append({"role": "user", "content": full_prompt})
    
    conversation_history = trim_conversation_history(conversation_history)
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=conversation_history,
        max_tokens=1000,
        temperature=0.7
    )
    
    conversation_history.append({"role": "assistant", "content": response.choices[0].message.content.strip()})
    conversation_history = trim_conversation_history(conversation_history)
    
    return response.choices[0].message.content.strip()

if __name__ == '__main__':
    # 클라이언트 인스턴스 생성
    client = create_openai_client()

    while True:
        user_input = input("당신: ")
        if user_input.lower() == "exit":
            print("대화를 종료합니다.")
            break
        answer = generate_answer(client, user_input)
        print("봇: ", answer)
