from django.shortcuts import render
import os
import urllib
from django.views import View
from team20.models import Products

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.prompts.prompt import PromptTemplate


def initialise_chat(initial_data):
    if not initial_data:
        print("No initial data")
        return

    # products = Products.objects.all()
    product_list = []

    for product in Products.objects.all()[:50]:
        print(product)
        product_list.append(str(product))


    init_string = """The following is an AI companion that is an expert on guitars. It always separates lists of products with newline characters after each product and does not give a number before each product.
    Here is all the data on the products available at GuitarGuitar. Use this data to help the customer get the right guitar that is sold at GuitarGuitar using your expertise for their request:
    """ + "".join(product_list) + """Current Conversation:
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

def orders(request):
    context_dict = {}
    return render(request, "team20/orders.html", context=context_dict)

class answer(View):
    def get(self, request):
        query = request.GET['query']
        context_dict = {"bot_answer": conversation.predict(input=query)}
        return render(request, 'team20/answer.html', context=context_dict)
