from django.shortcuts import render
import os
import urllib
from django.views import View

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.prompts.prompt import PromptTemplate


def initialise_chat(initial_data):
    if not initial_data:
        print("No initial data")
        return

    init_string = """The following is an AI companion that is an expert on guitars.

	Current Conversation:
	{history}
	Human: {input}
	AI Assistant:"""

    llm = ChatOpenAI(model_name='gpt-3.5-turbo-16k', temperature=0)

    PROMPT = PromptTemplate(input_variables=["history", "input"], template=init_string)
    conversation = ConversationChain(
        prompt=PROMPT,
        llm=llm,
        verbose=False,
        memory=ConversationBufferMemory(ai_prefix="AI Assistant"),
    )
    return conversation


conversation = initialise_chat("Hello!")


def index(request):
    context_dict = {}
    return render(request, "team20/index.html", context=context_dict)


def chat(request):
    return render(request, "team20/chat.html", context={})


class answer(View):
    def get(self, request):
        query = request.GET['query']
        context_dict = {"bot_answer": conversation.predict(input=query)}
        return render(request, 'team20/answer.html', context=context_dict)
