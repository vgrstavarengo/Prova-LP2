def avaliacao():
    import os

    arquivo = 'livros.txt'
    if not os.path.exists(arquivo):
        print(f"Erro: Arquivo '{arquivo}' não encontrado!")
        return

    livros = []
    with open(arquivo, 'r', encoding='utf-8') as f:
        for linha in f:
            linha = linha.strip()
            if linha:
                partes = linha.split(',', 1)
                if len(partes) == 2:
                    ano = partes[0].strip()
                    titulo = partes[1].strip()
                    livros.append({'ano': ano, 'titulo': titulo})

    print("\n" + "="*60)
    print("SISTEMA DE AVALIAÇÃO DE LIVROS")
    print("="*60 + "\n")

    avaliacoes = []

    for i, livro in enumerate(livros, 1):
        while True:
            try:
                print(f"{i}. {livro['ano']} - {livro['titulo']}")
                nota = float(input("   Digite a nota (0-10): "))

                if 0 <= nota <= 10:

                    print("   Status de leitura:")
                    print("     1 - Lido")
                    print("     2 - Lendo")
                    print("     3 - Na fila")

                    opc = input("   Escolha o status (1/2/3): ").strip()

                    
                    if opc == "1":
                        status = "lido"
                    elif opc == "2":
                        status = "lendo"
                    elif opc == "3":
                        status = "na_fila"
                    else:
                        print("   Opção inválida!\n")
                        continue

                    avaliacoes.append({
                        'ano': livro['ano'],
                        'titulo': livro['titulo'],
                        'nota': nota,
                        'status': status     
                    })

                    print(f"    Status registrado: {status}\n")
                    break

                else:
                    print("   Erro: A nota deve estar entre 0 e 10!\n")

            except ValueError:
                print("   Erro: Digite um número válido!\n")

 
    with open('livros_avaliacao.txt', 'w', encoding='utf-8') as f:
        f.write("ANO, TÍTULO, NOTA, STATUS\n")
        f.write("-"*60 + "\n")
        for av in avaliacoes:

            
            if av['status'] == "lido":
                status_txt = "Lido"
            elif av['status'] == "lendo":
                status_txt = "Lendo"
            else:
                status_txt = "Na fila"

            f.write(