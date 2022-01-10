import os
import openai


def gpt3(neighborhood,
         condition,
         apt_type,
         area_m2,
         lift,
         views,
         floor,
         room_type,
         accommodates,
         district,
         rooms,
         price,
         max_tokens=80):
    # Load your API key from an environment variable or secret management service
    openai.api_key = os.getenv('OPENAI_API_KEY')

    prompt = f'My customer asked me to write a descriptive sales pitch for his ' \
             f'house containing the following attributes: \n' \
             f'* Neighbourhood: {neighborhood}\n' \
             f'* Condition: {condition}\n' \
             f'* Apartment type: {apt_type}\n' \
             f'* Area: {area_m2}m2\n' \
             f'* Lift: {lift}\n' \
             f'* Views: {views}\n' \
             f'* Floor: {floor}\n' \
             f'* Room type: {room_type}\n' \
             f'* Bedrooms: {accommodates}\n' \
             f'* District: {district}\n' \
             f'* Rooms: {rooms}\n' \
             f'* Price: {price}\n' \
             f'I wrote the following sales pitch that includes the information about the house:\n'

    response = openai.Completion.create(
        engine='davinci',
        prompt=prompt,
        max_tokens=max_tokens
    )
    try:
        return response['choices'][0]['text']
    except Exception as e:
        print(e)
        return None
