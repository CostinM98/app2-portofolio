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
    
    I am looking for an entry-level position to kickstart my career in the Software Testing. I wish to work in a dynamic organisation that will contribute to my professional and personal growth while I contribute to the growth of the company as well as engage in opportunities to further the company’s goals.
    
    
    """


    st.info(content)

content2='''

Below you can find some apps I have built in Python(Only the Todo APP is available).Feel free to contact me!




'''

st.info(content2)

col3,emptyCol,col4=st.columns([1.5,0.5,1.5])

df=pandas.read_csv('data.csv',sep=';')
with col3:
    for index,row in df[0:10].iterrows():
        st.header(row['title'])

        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write('[Source Code](https://github.com/CostinM98/WebApp1)')


with col4:
    for index,row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row["description"])
        st.image('images/'+row['image'])

        print('Something')