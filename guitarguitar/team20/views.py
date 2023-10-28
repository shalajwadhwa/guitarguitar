from django.shortcuts import render
import os
import urllib
from django.views import View
from team20.models import Products
from llama_index import VectorStoreIndex, SimpleDirectoryReader

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.prompts.prompt import PromptTemplate
documents = SimpleDirectoryReader('data').load_data()
index = VectorStoreIndex.from_documents(documents)

from llama_index.memory import ChatMemoryBuffer
memory = ChatMemoryBuffer.from_defaults(token_limit=16000)
chat_engine = index.as_chat_engine(
    chat_mode="context",
    memory=memory,
    system_prompt=(
        """You are a chatbot for guitarguitar.co.uk, and are very knowledgeable on guitars. You have information on their products. Sales prices are in GBP.
        Use QtyInStock to give stock information. Be careful to get the product's exact price and stock. 
        You also have customer order information. Use Id to get a specific order ID. Use CustomerId to find orders made by that customer.
        Please be as accurate as possible.
        """
    ),
)

def index(request):
    context_dict = {}
    return render(request, "team20/index.html", context=context_dict)


def chat(request):
    return render(request, "team20/chat.html", context={})

def orders(request):
    context_dict = {}
    return render(request, "team20/orders.html", context=context_dict)

class answer(View):
    def get(self, request):
        query = request.GET['query']
        context_dict = {"bot_answer": chat_engine.chat(query)}
        return render(request, 'team20/answer.html', context=context_dict)
