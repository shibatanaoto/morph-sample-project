
import morph
from morph import MorphGlobalContext

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage


@morph.func
def chat(context: MorphGlobalContext):
    llm = ChatOpenAI(model="gpt-4o")
    messages = [HumanMessage(context.vars["prompt"])]
    for token in llm.stream(messages):
        yield token.content
