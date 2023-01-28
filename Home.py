import streamlit
import streamlit as st
import pandas
# st.set_page_config(layout='wide')


col1,col2=st.columns(2)

with col1:
    st.image('images/photo.png')

with col2:
    streamlit.title("Morun Costin-Andrei")
    content="""
    
    Seeking a career change to a position involving Software Testing. Driven self-starter and fast learner.
    
    
    """


    st.info(content)

content2='''

Below you can find some apps I have built in Python(for it will be only one maybe).Feel free to contact me!




'''

st.write(content2)

col3,emptyCol,col4=st.columns([1.5,0.5,1.5])

df=pandas.read_csv('data.csv',sep=';')
with col3:
    for index,row in df[0:10].iterrows():
        st.header(row['title'])

        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write('[Source Code](https://github.com/CostinM98/WebAppNo.1.git)')


with col4:
    for index,row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row["description"])
        st.image('images/'+row['image'])