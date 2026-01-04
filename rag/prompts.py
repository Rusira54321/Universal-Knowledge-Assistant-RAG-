from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

def get_qa_prompt():
    system_prompt = (
        "You are an intelligent assistant. Answer the question using only the information provided in the context and chat history. "
        "If the answer is not present in the context or chat history, politely say that you do not know. "
        "Your response must be a single plain text paragraph. "
        "Do not use lists numbering bullet points new lines symbols punctuation or special characters. "
        "Do not format the answer in any way. "
        "Use only descriptive sentences written with letters and spaces."
        "\n\n"
        "{context}"
        )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system",system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human","{question}"),
        ]
    )

    return prompt