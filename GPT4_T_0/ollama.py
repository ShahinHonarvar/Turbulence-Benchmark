from langchain.llms import Ollama


def run_ollama_model(model_params, text):
   
    model_name = model_params["model"]
    ollama = Ollama(model=model_name, num_ctx=model_params["max_tokens"])

    prompt = f'Here is a text specification delimited by angle brackets. Create Python code according to the text specification. <{text}> The Python code should be delimited only by triple backticks. Do not add comments to your code. Generate only one solution.'
    x = ollama(prompt)
    print(x)

    return x, prompt

