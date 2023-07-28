# Bring in dependencies
import webbrowser
import os
urL='https://www.google.com'
import os 
from apikey import apikey


from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper

import webbrowser

os.environ['OPENAI_API_KEY'] = apikey
# App Framework
prompt = input('What can I help you with?')

#Llms
llm = OpenAI(temperature=0.9)

#Webbrowser
webbrowser.register('chrome',None, webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))

if prompt:
    response = llm(prompt)
    print(response)


webbrowser.get('chrome').open_new_tab(urL)