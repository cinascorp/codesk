import openai
key=[]

openai.api_key_path = 'key'

print("\n                    ♾\n ")
cnt=input("Please enter any language you want to learn: ")

answers = []
stop_words = ["quit", "finish"]

while True:     
        sentences = input("\nWhat would you like me to generate as Code?\n")
        cnt += sentences
        if sentences.lower() in stop_words:
              break
        response = openai.Completion.create(
        prompt="Generate suitable code implements: " + sentences ,
        engine="text-davinci-002",
        max_tokens=2000,
        n=1,
        stop=stop_words,
        temperature=0.5,
    ).get("choices")[0].text
        answers.append(response)
        response_part1 = response[:1000]
        response_part2 = response[1000:2000]
        response_part3 = response[2000:3000]
        response_part4 = response[3000:]
        print(response_part1)
        print(response_part2)
        print(response_part3)
        print(response_part4)
        return
final_answer = "".join(answers)
print("Here's your final program:")
print(final_answer)
input("enter to exit...")
