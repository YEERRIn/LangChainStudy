# -*- encoding: euc-kr-*-
import os
from dotenv import load_dotenv
from langchain_teddynote import logging
from langchain_openai import ChatOpenAI
from langchain_teddynote.models import MultiModal
from langchain_teddynote.messages import stream_response

#API KEY �����ε� 
load_dotenv()
#logging.langsmith("CH01-Basic")

logging.langsmith("CH01-Basic", set_enable=False)



