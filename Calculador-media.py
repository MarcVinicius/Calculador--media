vezes = 0
soma = 0
nums = []
resposta = 'S'

while True:
    if resposta == 'S':
        if vezes == 0:
            num = input("Digite o primeiro número: ")
            vezes += 1
            nums.append(num)
        elif vezes > 0:
            num = input("Digite o próximo número: ")
            vezes += 1
            nums.append(num)
        
        resp = input("deseja adicionar mais um número? Responda com S ou N: ")
        if resp == 'N':
            resposta = 'N'
    else:
        if vezes > 1:
            break
        else:
            print("você precisa escolher mais de um número")
            resposta = 'S'

for i in nums:
    soma += int(i)

print(nums[0:])
print("Sua média é", (soma/len(nums)))