vezes = 0
soma = 0
nums = []
resposta = 'S'

while True:
    if resposta == 'S':
        if vezes == 0:
            num = input("Digite o primeiro número: ")
            if num.isnumeric() == True:
                nums.append(num)
                vezes += 1
            else:
                print("Você precisa escolher um número")
        elif vezes > 0:
            num = input("Digite o próximo número: ")
            if num.isnumeric() == True:
                vezes += 1
                nums.append(num)
            else:
                print("Você precisa escolher um número")
        
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