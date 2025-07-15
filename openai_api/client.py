from openai import OpenAI

client = OpenAI(
    api_key='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'
)


def get_car_ai_bio(model, brand, year):
    message = ''''
    Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisas específicas desse modelo.
    Descreva especificações técnicas desse modelo de carro.
    '''
    message = message.format(brand, model, year)
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
        {"role": "user", "content": message}
    ]
    )

    return response.choices[0].message.content