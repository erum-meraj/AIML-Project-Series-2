from bardapi import Bard
import os, streamlit
from streamlit_chat import message

os.environ["_BARD_API_KEY"] = "fQhKD30oYbAGDyJ4PSI-mcHYR_jeko2sEPgrwp4cn4e3Vb_p8aNke6t5dRkVrLlDVyacfg."

streamlit.title("College admission chatbot")

def response(prompt):
    message = Bard().get_answer("Consider your are the admissions expert of XYZ University. the user wants to get an admission into XYZ institute and asks queries about admission. Here is more information about the institute: required SAT score = >1200, documents = marksheet, aadhar card, add more general documents from your side. XYZ university has the same admission procedure as Harvard so take information from there too. The question from the user is: " + str(prompt))['content']
    return message

def user_inp():
    inp = streamlit.text_input("Enter query")
    return inp

if 'generate' not in streamlit.session_state:
    streamlit.session_state['generate'] = []
if 'past' not in streamlit.session_state:
    streamlit.session_state['past'] = []



inp_txt = user_inp()

if inp_txt:
    out = response(inp_txt)
    streamlit.session_state.generate.append(out)
    streamlit.session_state.past.append(inp_txt)

if streamlit.session_state['generate']:
    for i in range(len(streamlit.session_state['generate'])-1, -1, -1):
        message(streamlit.session_state["past"][i], is_user=True, key=str(i) + '_user')
        message(streamlit.session_state['generate'][i], key=str(i))


