from emoji import generate_landspace,answer_number
import os

output = generate_landspace(3000,3000,50)
print(output)

os.makedirs('outputs',exist_ok=True)

with open('outputs/output.txt',"a", encoding='utf-8') as file:
    file.write(output)