from flask import Flask, request, jsonify

app = Flask(__name__)

def generate_palette(input):
    import openai

    openai.api_key = "sk-or-vv-3f9999cd4a1b7fea230a6fabd0403da0f64bbe7d2ccc668b3765e3d3780f62c0"

    openai.base_url = "https://api.vsegpt.ru/v1/"

    #prompt = """Generate a palette of 4 matching colors for a designer
    #           my text description. Write only their rgb codes. Here's the description: """
    
    prompt = """Сгенерируй 4 сочетающихся цвета для дизайнера по моему текстовому описанию. Напиши только эти
                цвета в формате HEX и пронумеруй их. Больше ничего писать не нужно"""
    
    prompt += input

    messages = []
    messages.append({"role": "user", "content": prompt})

    response_big = openai.chat.completions.create(
        model="openai/gpt-4o",
        messages=messages,
        temperature=0.7,
        n=1,
        max_tokens=3000,
    )

    #print("Response BIG:",response_big)
    response = response_big.choices[0].message.content
    return response

def collect_hex(text):
    hexs = []
    for i in range(len(text)):
        if text[i] == "#":
            hexs.append(str(text[i:i + 7]))
    dct = {}
    for index, color in enumerate(hexs):
        dct[index] = color
    res = []
    res.append(dct)
    return res
    

@app.route('/generate_palette', methods=['GET'])
def generate_color_api():
    colors = generate_color()
    return jsonify(colors)

if __name__ == '__main__':
    app.run(debug=True)
