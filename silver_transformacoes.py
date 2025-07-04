import os
import pandas as pd
import gcsfs

def processar_dados_gcs(bucket_name, chave_json, formato_entrada, caminho_particionado,
                        limpar_colunas, pasta_saida_local, grupos, particionado=False):
    # Autentica no GCS
    fs = gcsfs.GCSFileSystem(token=chave_json)

    # Lista arquivos no bucket
    if particionado:
        arquivos = fs.glob(f'{bucket_name}/{caminho_particionado}*.{formato_entrada}')
    else:
        arquivos = [f'{bucket_name}/{caminho_particionado}.{formato_entrada}']

    for caminho_completo in arquivos:
        print(f'Processando {caminho_completo}...')
        nome_base = os.path.splitext(os.path.basename(caminho_completo))[0]

        # Lê o Parquet diretamente do GCS
        with fs.open(caminho_completo, 'rb') as f:
            df = pd.read_parquet(f)

        # Remove colunas que o usuário quer limpar (exceto NU_INSCRICAO)
        colunas_a_remover = [col for col in limpar_colunas if col != 'NU_INSCRICAO']
        df.drop(columns=[col for col in colunas_a_remover if col in df.columns], inplace=True)

        # Para cada grupo de colunas, cria um arquivo separado
        for grupo, colunas in grupos.items():
            colunas_necessarias = colunas.copy()

            # Garante que NU_INSCRICAO esteja presente em prova_objetiva
            if grupo == "prova_objetiva" and "NU_INSCRICAO" not in colunas_necessarias:
                colunas_necessarias.insert(0, "NU_INSCRICAO")  # adiciona ao início

            # Filtra colunas que realmente existem no DataFrame
            colunas_existentes = [col for col in colunas_necessarias if col in df.columns]
            if not colunas_existentes:
                continue

            df_subset = df[colunas_existentes]

            caminho_saida = f"{bucket_name}/{pasta_saida_local}/{grupo}/{nome_base}_{grupo}.parquet"
            print(f'Salvando arquivo {caminho_saida}...')

            with fs.open(caminho_saida, 'wb') as f_out:
                df_subset.to_parquet(f_out, index=False)

    print("Processamento finalizado.")

if __name__ == "__main__":
    bucket_name = 'enem-buckett'
    chave_json = "C:/Users/neusa/OneDrive/Documentos/erick/IFNMG/Bancoded/Trabalho/Chave/erick-pedro-giovanni-db2288d4b64b.json"

    formato_entrada = 'parquet'
    caminho_particionado = 'bronze/parquet/MICRODADOS_ENEM_2023_chunk_'

    remover_colunas = ['coluna82', 'coluna342', 'coluna343', 'coluna344', 'coluna345', 'coluna346', 'coluna347', 'coluna348', 'coluna349']

    grupos_dados = {
        "participante": [
            "NU_INSCRICAO", "NU_ANO", "TP_FAIXA_ETARIA", "TP_SEXO", "TP_ESTADO_CIVIL", "TP_COR_RACA",
            "TP_NACIONALIDADE", "TP_ST_CONCLUSAO", "TP_ANO_CONCLUIU", "TP_ESCOLA", "TP_ENSINO", "IN_TREINEIRO"
        ],
        "escola": [
            "CO_MUNICIPIO_ESC", "NO_MUNICIPIO_ESC", "CO_UF_ESC", "SG_UF_ESC",
            "TP_DEPENDENCIA_ADM_ESC", "TP_LOCALIZACAO_ESC", "TP_SIT_FUNC_ESC"
        ],
        "local_de_aplicacao_da_prova": [
            "CO_MUNICIPIO_PROVA", "NO_MUNICIPIO_PROVA", "CO_UF_PROVA", "SG_UF_PROVA"
        ],
        "prova_objetiva": [
            "TP_PRESENCA_CN", "TP_PRESENCA_CH", "TP_PRESENCA_LC", "TP_PRESENCA_MT",
            "CO_PROVA_CN", "CO_PROVA_CH", "CO_PROVA_LC", "CO_PROVA_MT",
            "NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT",
            "TX_RESPOSTAS_CN", "TX_RESPOSTAS_CH", "TX_RESPOSTAS_LC", "TX_RESPOSTAS_MT",
            "TP_LINGUA", "TX_GABARITO_CN", "TX_GABARITO_CH", "TX_GABARITO_LC", "TX_GABARITO_MT"
        ],
        "dados_da_redacao": [
            "TP_STATUS_REDACAO", "NU_NOTA_COMP1", "NU_NOTA_COMP2",
            "NU_NOTA_COMP3", "NU_NOTA_COMP4", "NU_NOTA_COMP5", "NU_NOTA_REDACAO"
        ],
        "dados_do_questionario_socioeconomico": [
            "Q001", "Q002", "Q003", "Q004", "Q005", "Q006", "Q007", "Q008",
            "Q009", "Q010", "Q011", "Q012", "Q013", "Q014", "Q015", "Q016",
            "Q017", "Q018", "Q019", "Q020", "Q021", "Q022", "Q023", "Q024", "Q025"
        ]
    }

    processar_dados_gcs(
        bucket_name=bucket_name,
        chave_json=chave_json,
        formato_entrada=formato_entrada,
        caminho_particionado=caminho_particionado,
        limpar_colunas=remover_colunas,
        pasta_saida_local='silver/parquet',
        grupos=grupos_dados,
        particionado=True
    )
