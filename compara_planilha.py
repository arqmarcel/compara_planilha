import pandas as pd

def comparar_estrutura_excel(arquivo_original, novo_arquivo):
    # Carregando as bases (original e nova)
    try:
        df_model = pd.read_excel(arquivo_original)
        df_new = pd.read_excel(novo_arquivo)
    except FileNotFoundError:
        print("Erro: Um ou ambos os arquivos não foram encontrados.")
        return
    except ValueError:
        print("Erro: Problema ao ler os arquivos. Verifique se são arquivos Excel válidos.")
        return
    except Exception as e:
        print(f"Erro inesperado ao carregar os arquivos: {e}")
        return

    if df_model.columns.equals(df_new.columns):
        print("A estrutura dos arquivos é a mesma, incluindo a ordem das colunas.")
    else:
        if set(df_model.columns) == set(df_new.columns):
            print("Os arquivos possuem as mesmas colunas, mas em ordens diferentes.")
        else:
            missing_columns = set(df_model.columns) - set(df_new.columns)
            additional_columns = set(df_new.columns) - set(df_model.columns)

            if missing_columns:
                print(f"As colunas {sorted(missing_columns)} estão faltando no novo arquivo.")
            if additional_columns:
                print(f"As colunas {sorted(additional_columns)} foram adicionadas no novo arquivo.")
        
        print("Ordem no arquivo original:", list(df_model.columns))
        print("Ordem no novo arquivo:", list(df_new.columns))

# Usando a função
comparar_estrutura_excel('arquivo_original.xlsx', 'novo_arquivo.xlsx')