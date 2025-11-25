def top_livros():
    

    import os

    arquivo = "livros_recomendados.txt"

    if not os.path.exists(arquivo):
        print(f"Erro: Arquivo '{arquivo}' não encontrado!")
        return

    livros = []

    with open(arquivo, "r", encoding="utf-8") as f:
        linhas = f.readlines()

        for linha in linhas:
            linha = linha.strip()
            if not linha:
                continue

            partes = linha.split(',')

            livro = {}

            for p in partes:
                p = p.strip()

                if p.startswith("ANO:"):
                    livro["ano"] = p.replace("ANO:", "").strip()

                elif p.startswith("TÍTULO:"):
                    livro["titulo"] = p.replace("TÍTULO:", "").strip()

                elif p.startswith("AUTOR:"):
                    livro["autor"] = p.replace("AUTOR:", "").strip()

                elif p.startswith("NOTA:"):
                    livro["nota"] = float(p.replace("NOTA:", "").strip())

                elif p.startswith("STATUS DE LEITURA:"):
                    livro["status"] = p.replace("STATUS DE LEITURA:", "").strip()

            if "nota" in livro:  
                livros.append(livro)


    livros.sort(key=lambda x: x["nota"], reverse=True)

    
    print(f"\n{'='*60}")
    print("RANKING DE LIVROS - DO MELHOR PARA O PIOR")
    print(f"{'='*60}\n")

    for i, livro in enumerate(livros, 1):
        print(f"{i:2d}. [{livro['nota']:4.1f}] {livro['titulo']} ({livro['ano']}) - {livro['autor']}")

    print(f"\n{'='*60}\n")