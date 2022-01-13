import os
import openai


def gpt3(neighborhood,
         condition,
         area_m2,
         views,
         floor,
         accommodates,
         district,
         rooms,
         max_tokens=120):
    # Load your API key from an environment variable or secret management service
    openai.api_key = os.getenv('OPENAI_API_KEY')

    prompt = f'My customer asked me to write a descriptive sales pitch for his ' \
             f'house containing the following attributes: \n' \
             f'* District: {district}\n' \
             f'* Neighbourhood: {neighborhood}\n' \
             f'* Condition: {condition}\n' \
             f'* Area: {area_m2} m2\n' \
             f'* Views: {views}\n' \
             f'* Floor: {floor}\n' \
             f'* Rooms: {rooms}\n' \
             f'* Bedrooms: {accommodates}\n' \
             f'I wrote the following sales pitch that includes the information about the house:\n'

    try:
        response = openai.Completion.create(
            engine='davinci',
            prompt=prompt,
            max_tokens=max_tokens
        )
        return response['choices'][0]['text']
    except Exception as e:
        print(e)
        return None
