import streamlit as st
import streamlit.components.v1 as components
# def render_ato_html(conteudo, index):
#     st.markdown(f"#### Ato {index}")
#     st.markdown(
#         f"""
#              <div style='border:1px solid #ccc; padding:10px;overflow:auto; background-color:#f9f9f9;'>
#              {conteudo}
#             </div>
#         """,
#         unsafe_allow_html=True
#     )

# def render_ato_selecao (texto):
#     html_code = f"""
#         <div id="seletor" style="border:1px solid #ccc; padding:10px; max-height:400px; overflow:auto; background-color:#f9f9f9;">
#             {texto}
#         </div>
        
#         <script>
#             const div = document.getElementById("seletor");
#             div.addEventListener("mouseup", function () {{
#                 var selectedText = window.getSelection().toString();
#                 if (selectedText.lenght > 0) {{
#                     const streamlitInput = window.parent;
#                     streamlitInput.postMessage({{ isStreamlitMessage: true, type: "streamlit:setComponentValue", value: selectedText }}, "*");
#                 }}
#             }});
#         <\script> 
#     """
#     selected = components.html(html_code, height = 400)
#     return selected

# def render_conteudo_salvo(conteudo):

    # max-height:200px; 