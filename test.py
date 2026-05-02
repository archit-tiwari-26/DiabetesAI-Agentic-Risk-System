# import os
# from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI

# def main():
#     load_dotenv()

#     api_key = os.getenv("GOOGLE_API_KEY")

#     if not api_key:
#         raise ValueError("❌ GOOGLE_API_KEY not found in .env")

#     llm = ChatGoogleGenerativeAI(
#         model="gemini-1.5-flash-latest",
#         temperature=0.7,
#         google_api_key=api_key
#     )

#     response = llm.invoke("Say hello and confirm the API is working.")

#     print("\n✅ Response from Gemini:\n")
#     print(response.content)


# if __name__ == "__main__":
#     main()
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7,
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    convert_system_message_to_human=True
)

print(llm.invoke("Explain how AI works in a few words").content)