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
memory = ChatMemoryBuffer.from_defaults(token_limit=1500)
chat_engine = index.as_chat_engine(
    chat_mode="context",
    memory=memory,
    system_prompt=(
        """You are a chatbot for guitarguitar.co.uk. You have information on their products. Sales prices are in GBP. Be careful to get the exact product's price.
        Use QtyInStock to give stock information. You will also have customer order information. The 'id' refers to the order ID, and 'customerid' is for
        the customer's ID. If a customer gives you their customer ID, only give information relating to the orders made with their unique ID ('customerid').
        Make sure you check order information in one message."""
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
