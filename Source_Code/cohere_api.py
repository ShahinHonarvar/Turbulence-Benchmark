import os
import cohere

API_KEY = os.getenv('COHERE_KEY')
co = cohere.Client(API_KEY)


def get_code(model_params, prompt):
    response = co.generate(
        prompt=prompt,
        model=model_params['model'],

        # Can only be set to 0 if return_likelihoods is set to ALL to get the likelihood of the prompt.
        max_tokens=model_params['max_tokens'],

        # Defaults to 0.75, min value of 0.0, max value of 5.0. A non-negative float that tunes the degree of
        # randomness in generation. Lower temperatures mean less random generations.
        temperature=model_params['temperature'],

        # Defaults to 0.0, min value of 0.0, max value of 1.0. Can be used to reduce repetitiveness of generated tokens.
        # The higher the value, the stronger a penalty is applied to previously present tokens, proportional to
        # how many times they have already appeared in the prompt or prior generation.
        frequency_penalty=model_params['frequency_penalty'],

        # Defaults to 0.0, min value of 0.0, max value of 1.0. Can be used to reduce repetitiveness of generated tokens.
        # Similar to frequency_penalty, except that this penalty is applied equally to all tokens that have already
        # appeared, regardless of their exact frequencies.
        presence_penalty=model_params['presence_penalty'],
    )

    return response


def run_cohere_model(model_params, text):

    prompt = f'Here is a text specification delimited by angle brackets. Create Python code according to the text specification. The Python code should not contain any comments. The Python code should be delimited only by triple backticks. <{text}>'
    response = get_code(model_params, prompt)

    return response, prompt
