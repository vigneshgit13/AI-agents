import streamlit as st
from openai import OpenAI
import os
GROQ_API_KEY='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'
client=OpenAI(api_key=GROQ_API_KEY,base_url='https://api.groq.com/openai/v1')
st.set_page_config(page_title='GOAL BASED MEDICAL AGENT',layout='centered')
st.title('gOAL BASED MEDICAL ASSISTANT')
st.markdown('decribe your health conditions or symptoms.The AI will decide whether you need rest or doctor or emergency care.')
user_input= st.text_area('Describe your symptoms how you are feeling:')
if('chat_history' not in st.session_state):
    st.session_state.chat_history = []
if(user_input):
    st.session_state.chat_history.append({'role':'user','content':'user_input'})
    with st.spinner('analysing your condition'):
        try:
            messages=[
                {'role':'system','content':
                 'you are a goal based medical assistant. your goal is to analyse user symptom and advise one of the following'
                 '(1) rest at home ,(2) consult a doctor, (3) go to emergency. be cautious!. ask followup questions if needed'  
                 'Be clear and structured in response'
                 }
            ] + st.session_state.chat_history
            response = client.chat.completions.create(model='llama3-8b-8192',messages=messages,temperature=0.5,max_tokens=800)
            AI_reply=response.choices[0].message.content
            st.session_state.chat_history.append({'role':'assistant','content':AI_reply})
            st.success('recommendation:')
            st.markdown(AI_reply)
        except Exception as e:
            st.error(f'error:{str(e)}')

