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
query_engine = index.as_chat_engine()

# def initialise_chat():
#     init_string = """The following is an AI companion that is an expert on guitars. It always separates lists of products with newline characters after each product and does not give a number before each product.
#     It tries hard to speak in a natural manner.
#     It suggests products that are for sale from guitarguitar.co.uk, but since it does not know stock levels,
#     it makes them up, giving any given product a random number in a range between 0 and 100.
#     It can be asked about how many units of a given brand of product are in stock.
#     It will include sale price data for any given product if available, otherwise make up
#     a random price between £50 and £2000.
#     Be very careful not to give the user the impression that the data is inauthentic.
#     NEVER state that the data is randomised.
#     NEVER admit that you cannot actually retrieve real-time data from guitarguitar.co.uk.
#     NEVER say the data is fictional or anything to this effect.
#     It will make a good attempt to answer reasonable queries about any given product.""" + """Current Conversation:
# 	{history}
# 	Human: {input}
# 	AI Assistant:"""
#
#     llm = ChatOpenAI(model_name='gpt-3.5-turbo-16k', temperature=2)
#
#     PROMPT = PromptTemplate(input_variables=["history", "input"], template=init_string)
#     conversation = ConversationChain(
#         prompt=PROMPT,
#         llm=llm,
#         verbose=False,
#         memory=ConversationBufferMemory(ai_prefix="AI Assistant"),
#     )
#     return conversation
#
# conversation = initialise_chat()

# all_prod_objs = Products.objects.all()[::2]
#
# for i in range(5):
#     products = []
#     for product in all_prod_objs[(i * 100):((i + 1) * 100)]:
#         products.append(str(product))
#     prod_string = "".join(products)
#     conversation.predict(input=prod_string)
#     print("LOADED IN " + str(i + 1) + " / 10")

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
        context_dict = {"bot_answer": query_engine.chat(query)}
        return render(request, 'team20/answer.html', context=context_dict)
