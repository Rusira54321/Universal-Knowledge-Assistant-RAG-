from langchain_core.prompts import ChatPromptTemplate

def get_qa_prompt():
    system_prompt = (
        "You are an intelligent chatbot. Use only the following context to answer the question. If you don't know  the answer , just say that you don't know in woderful way."
        "\n\n"
        "{context}"
        )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system",system_prompt),
            ("human","{question}"),
        ]
    )

    return prompt