import pandas as pd


def carregar_arquivo(caminho):
    """
    Função auxiliar para carregar diferentes formatos de arquivo.
    
    Args:
        caminho (str): Caminho para o arquivo a ser carregado
        
    Returns:
        pandas.DataFrame: DataFrame carregado ou None em caso de erro
    """
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


def comparar_estrutura_arquivos(arquivo_original, novo_arquivo):
    """
    Compara a estrutura de dois arquivos (Excel, CSV ou JSON), verificando suas colunas.
    
    Args:
        arquivo_original (str): Caminho para o arquivo original
        novo_arquivo (str): Caminho para o novo arquivo
        
    Returns:
        bool: True se a comparação foi realizada com sucesso, False caso contrário
    """
    # Carregando os arquivos
    df_model = carregar_arquivo(arquivo_original)
    df_new = carregar_arquivo(novo_arquivo)
    
    # Verificando se os arquivos foram carregados com sucesso
    if df_model is None or df_new is None:
        return False
    
    # Comparando colunas
    if df_model.columns.equals(df_new.columns):
        print("A estrutura dos arquivos é a mesma, incluindo a ordem das colunas.")
    else:
        colunas_model = set(df_model.columns)
        colunas_new = set(df_new.columns)
        
        if colunas_model == colunas_new:
            print("Os arquivos possuem as mesmas colunas, mas em ordens diferentes.")
        else:
            missing_columns = colunas_model - colunas_new
            additional_columns = colunas_new - colunas_model
            
            if missing_columns:
                print(f"As colunas {sorted(missing_columns)} estão faltando no novo arquivo.")
            if additional_columns:
                print(f"As colunas {sorted(additional_columns)} foram adicionadas no novo arquivo.")
        
        print("Ordem no arquivo original:", list(df_model.columns))
        print("Ordem no novo arquivo:", list(df_new.columns))
    
    return True


if __name__ == "__main__":
    # Exemplo de uso com diferentes formatos de arquivo
    # comparar_estrutura_arquivos("dados_originais.xlsx", "dados_novos.csv")
    # comparar_estrutura_arquivos("dados_originais.json", "dados_novos.xlsx")