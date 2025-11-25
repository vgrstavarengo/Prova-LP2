def top_5_livros():
    arquivo = "livros_recomendados.txt"
    livros = []

    with open(arquivo, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if not linha:
                continue


            partes = linha.split(",")
            if len(partes) < 6:
                continue

            ano = partes[0].replace("ANO:", "").strip()
            titulo = partes[1].replace("TÍTULO:", "").strip()
            autor = partes[2].replace("AUTOR:", "").strip()
            nota = partes[3].replace("NOTA:", "").strip()
            status = partes[5].replace("STATUS DE LEITURA:", "").strip()


            try:
                nota = float(nota)
            except:
                continue

            
            if status.lower() in ["lido", "lendo"]:
                livros.append({
                    "ano": ano,
                    "titulo": titulo,
                    "autor": autor,
                    "nota": nota,
                    "status": status
                })

  
    livros.sort(key=lambda x: x["nota"], reverse=True)


    top5 = livros[:5]

    print("\n=== TOP 5 MAIORES NOTAS (Lido / Lendo) ===")
    for i, livro in enumerate(top5, start=1):
        print(f"{i}. {livro['titulo']} - Nota {livro['nota']} ({livro['status']})")

    return top5