import streamlit as st
##from doe_data.acesso_bd import engine
from sqlalchemy import text
import requests
from doe_data.queries import get_publicacoes, get_atos
#from utils.visualizacao import render_ato_selecao
from utils.tools import highlight_text

st.set_page_config(layout="wide")
st.title("Visualizador de Publicações")

publicacoes = get_publicacoes()
links = [row[0] for row in publicacoes]
ids = [row[1] for row in publicacoes]
conteudos_link = [row[2] for row in publicacoes]

if 'index' not in st.session_state:
    st.session_state.index = 0

col1, col2 = st.columns ([1,1])
with col1:
    if st.button("Anterior") and st.session_state.index > 0:
        st.session_state.index -=1
with col2:
    if st.button("Próximo") and st.session_state.index < len(links) -1:
        st.session_state.index +=1

st.markdown("### Buscar trecho no conteúdo")
termo = st.text_input ("Copie aqui o trecho do ato para destacar no conteúdo")

if links:
    i = st.session_state.index
    st.write(f"Publicacao {i+1} de {len(links)}")
    st.write("Link:", links[i])

    col_ato, col_texto, col_link = st.columns([2,1.5,1.5])

    with col_ato:
        st.markdown("### Atos Relacionados")
        atos = get_atos(ids[i])
        if atos:
            for j, ato in enumerate(atos, start=1):
                st.markdown(f"#### Ato {j}")
                st.markdown(
                    f"""
                    <div style='border:1px solid #ccc; padding:10px; overflow:auto; background-color:#f9f9f9;'>
                    {ato[0]}
                </div>
                    """,
                    unsafe_allow_html=True
                )
        # if atos:
        #     for j, ato in enumerate (atos,start =1):
        #         termo_selecionado = render_ato_selecao(ato[0])
        else:
            st.info("Nenhum conteúdo relacionado")
#  termo = streamlit_js_eval(js_expressions='window.getSelection().toString()', key="texto_selecionado")

    with col_texto:
        st.markdown("### Conteúdo (resumo em texto)")
        # termo = termo_selecionado.value if termo_selecionado and hasattr(termo_selecionado, "value") else ""
        texto_formatado = highlight_text(conteudos_link[i], termo)
        st.markdown(
            f"""
            <div    style='border:1px solid #ccc; padding:10px; overflow:auto; background-color:#f0f0f0;'>
                {texto_formatado}
            </div>
            """,
            unsafe_allow_html=True
            )

    with col_link:
        st.markdown("### Link carregado")
        try:
            response = requests.get(links[i], verify=False)
            response.raise_for_status()
            st.markdown(response.text, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Erro ao carregar o link: {e}")
else:
    st.warning("Nenhum dado encontrado")







# query_view = text("SELECT link, id FROM vw_publicacao")

# with engine.connect() as conn:
#     result = conn.execute(query_view)
#     #row = result.fetchone()
#     registros = result.fetchall()
#     links = [row[0] for row in registros] # Lista com todos os links
#     publicacao_ids = [row[1] for row in registros]

# #inicializa o índice da sessão se não estiver definido
# if 'index' not in st.session_state:
#     st.session_state.index = 0

# # Botões de navegação
# btn1, btn2 = st.columns([1,1])

# with btn1:
#     if st.button("Anterior") and st.session_state.index > 0:
#         st.session_state.index -=1
# with btn2:
#     if st.button("Próximo") and st.session_state.index < len(links) -1:
#         st.session_state.index +=1

# # Pega o link atual com base no índice
# if links:
#     current_index = st.session_state.index
#     current_link = links[current_index]
#     current_id = publicacao_ids[current_index]
#     st.title ("Visualizador de Publicações")
#     st.write(f"Publicação {st.session_state.index + 1} de {len(links)}")
#     st.write("Link da publicação:", current_link)

#     #layout com 2 colunas lado a lado
#     col1, col2 = st.columns([2,1])
#     with col1:
#         try:
#             response = requests.get(current_link, verify = False) #ignora SSL 
#             response.raise_for_status()
#             st.markdown(response.text, unsafe_allow_html=True)
#         except Exception as e:
#             st.error(f"Erro ao carregar o conteúdo: {e}")
#     with col2:
#         st.markdown("###Registos relacionados (conteúdo do ato)")
#         # consulta dos registros relacionados ao publicacao_id
#         query_ato = text ("""
#                     SELECT conteudo_ato
#                     FROM processing.ato
#                     WHERE publicacao_id = :id
#                     """)
#         with engine.connect() as conn:
#             results_ato = conn.execute(query_ato, {"id": current_id}).fetchall()
#         if results_ato:
#             for i, row in enumerate(results_ato, start=1):
#                 st.markdown(f"#### Ato {i}")
#                 # Scroll com altura fixa via CSS inline
#                 st.markdown(
#                     f"""
#                     <div style='border:1px solid #ccc; padding:10px; max-height:200px; overflow:auto; background-color:#f9f9f9;'>
#                     {row[0]}
#                     </div>
#                     """,
#                     unsafe_allow_html=True
#                 )
#         else:
#             st.info("Nenhum conteúdo relacionado encontrado.")
# else:
#     st.warning("Nenhum link encontrado.")



# st.title ("Visualizador de Publicações")
# if row:
#     link = row[0]
#     st.write("Link da publicação:", link)
#     try:
#         response = requests.get(link, verify = False) #ignora verificação SSL, rodando interno em teste
#         response.raise_for_status()
#         st.markdown(response.text, unsafe_allow_html=True)
#     except Exception as e:
#         st.error(f"Erro ao carregar o conteúdo: {e}")
# else:
#     st.write("Nenhum link encontrado.")


# if row:
#     st.text_area("Conteúdo:", row[0], height=400)
# else:
#     st.write("Nenhum dado encontrado.")