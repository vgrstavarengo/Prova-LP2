livros = []

with open("livros_recomendados.txt"), "r", encoding="utf-8") as f:
    for linha in f:
        partes = linha.strip().split(',')
        livro = {}
        for p in partes:
            p = p.strip()
            if p.startswith("ANO:"):
                livro["ano"] = int(p.replace("ANO:", "").strip())
            elif p.startswith("TÍTULO:"):
                livro["titulo"] = p.replace("TÍTULO:", "").strip()
            elif p.startswith("AUTOR:"):
                livro["autor"] = p.replace("AUTOR:", "").strip()
            elif p.startswith("NOTA:"):
                livro["nota"] = int(p.replace("NOTA:", "").strip())
            elif p.startswith("STATUS DE LEITURA:"):
                livro["status"] = p.replace("STATUS DE LEITURA:", "").strip()

        livros.append(livro)


livros_ordenados = sorted(livros, key=lambda x: x["nota"], reverse=True)


for livro in livros_ordenados:
    print(f"{livro['titulo']} — Nota {livro['nota']} — Autor: {livro['autor']}")