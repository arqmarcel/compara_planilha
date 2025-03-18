import pandas as pd

def comparar_estrutura_excel(arquivo_original, novo_arquivo):
    # Função auxiliar para carregar arquivos
    def carregar_arquivo(caminho):
        try:
            if caminho.endswith('.xlsx') or caminho.endswith('.xls'):
                return pd.read_excel(caminho)
            elif caminho.endswith('.csv'):
                return pd.read_csv(caminho)
            elif caminho.endswith('.json'):
                return pd.read_json(caminho)
            else:
                print(f"Erro: Formato de arquivo não suportado ({caminho}).")
                return None
        except FileNotFoundError:
            print(f"Erro: O arquivo {caminho} não foi encontrado.")
            return None
        except ValueError:
            print(f"Erro: Problema ao ler o arquivo {caminho}. Verifique se o formato é válido.")
            return None
        except Exception as e:
            print(f"Erro inesperado ao carregar o arquivo {caminho}: {e}")
            return None

    # Carregando os arquivos
    df_model = carregar_arquivo(arquivo_original)
    df_new = carregar_arquivo(novo_arquivo)

    if df_model is None or df_new is None:
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
comparar_estrutura_excel('arquivo_original.xlsx', 'novo_arquivo.csv')
