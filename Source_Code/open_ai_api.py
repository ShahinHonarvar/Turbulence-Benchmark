import os
import openai

openai.api_key = os.getenv('OPEN_AI_KEY')
openai.Model.list()


def get_code(model_params, prompt):
    response = openai.ChatCompletion.create(
        model=model_params['model'],

        # Defaults to 16.
        # The maximum number of tokens to generate in the completion.
        # The token count of your prompt plus max_tokens cannot exceed the model's context length.
        # Most models have a context length of 2048 tokens (except for the newest models, which support 4096).
        max_tokens=model_params['max_tokens'],

        # Defaults to 1.
        # What sampling temperature to use, between 0 and 2.
        # Higher values like 0.8 will make the output more random,
        # while lower values like 0.2 will make it more focused and deterministic.
        # We generally recommend altering this or top_p but not both.
        temperature=model_params['temperature'],

        # Defaults to 0.
        # Number between -2.0 and 2.0.
        # Positive values penalize new tokens based on whether they appear in the text so far,
        # increasing the model's likelihood to talk about new topics.
        presence_penalty=model_params['presence_penalty'],

        # Defaults to 0.
        # Number between -2.0 and 2.0.
        # Positive values penalize new tokens based on their existing frequency in the text so far,
        # decreasing the model's likelihood to repeat the same line verbatim.
        frequency_penalty=model_params['frequency_penalty'],

        messages=[{'role': 'user', 'content': prompt}],
    )

    return response


def run_open_ai_model(model_params, text):

    prompt = f'Here is a text specification delimited by angle brackets. Create Python code according to the text specification. <{text}> The Python code should not contain any comments. The Python code should be delimited only by triple backticks.'
    response = get_code(model_params, prompt)

    return response, prompt
