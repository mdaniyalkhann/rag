from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from dotenv import load_dotenv
import argparse

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument("--task", default="return a list of numbers")
parser.add_argument("--language", default="python")
args = parser.parse_args()

llm = OpenAI()

code_template = PromptTemplate(
    input_variables=["task", "language"],
    template="write a very short program that will {task} in {language}",
)

next_template = PromptTemplate(
    input_variables=["code", "language"],
    template="write a test for the following code in {language}:\n\n{code}",
)

code = LLMChain(llm=llm, prompt=code_template, output_key="code")
test = LLMChain(llm=llm, prompt=next_template, output_key="test")

seq = SequentialChain(
    chains=[code, test],
    input_variables=["task", "language"],
    output_variables=["code", "test"],
)


result = seq({"task": args.task, "language": args.language})

print(result["code"])
print(result["test"])
