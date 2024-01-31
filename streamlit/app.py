import streamlit as st
import plotly.express as px
import pandas as pd


st.set_page_config(layout="wide")

st.write('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

st.title('Mario Kart Optimization')

col1, col2, col3 = st.columns([2,4,2])


with col1:

    with st.container(border=True):

        st.subheader("Stats")

        tab1, tab2, tab3, tab4 = st.tabs(["Speed", "Acceleration", "Traction", "Handling"])

        with tab1:
            is_sl= st.toggle("Speed Ground", value=True)
            sl_slider= st.slider("SL", 0, 20, 15, label_visibility="collapsed")

            is_sw= st.toggle("Speed Water", value=False)
            sw_slider= st.slider("SW", 0, 20, 15, label_visibility="collapsed")

            is_sa= st.toggle("Speed Air", value=False)
            sa_slider= st.slider("SA", 0, 20, 15, label_visibility="collapsed")

            is_sg= st.toggle("Speed Anti-Gravity", value=False)
            sg_slider= st.slider("SG", 0, 20, 15, label_visibility="collapsed")
            

        with tab2:

            is_ac= st.toggle("Acceleration", value=True)
            ac_slider= st.slider("AC", 0, 20, 15, label_visibility="collapsed")

            is_mt= st.toggle("Mini-Turbo", value=True)
            mt_slider= st.slider("MT", 0, 20, 15, label_visibility="collapsed")

            is_wg= st.toggle("Weight", value=False)
            wg_slider= st.slider("WG", 0, 20, 15, label_visibility="collapsed")

            is_iv= st.toggle("Invincibility", value=False)
            iv_slider= st.slider("IV", 0, 20, 15, label_visibility="collapsed")

        with tab3:

            is_on= st.toggle("On-Road Traction", value=False)
            on_slider= st.slider("ON", 0, 20, 15, label_visibility="collapsed")

            is_of= st.toggle("Off-Road Traction", value=False)
            of_slider= st.slider("OF", 0, 20, 15, label_visibility="collapsed")

        with tab4:

            is_tl= st.toggle("Ground Handling", value=False)
            tl_slider= st.slider("TL", 0, 20, 15, label_visibility="collapsed")

            is_tw= st.toggle("Water Handling", value=False)
            tw_slider= st.slider("TW", 0, 20, 15, label_visibility="collapsed")

            is_ta= st.toggle("Air Handling", value=False)
            ta_slider= st.slider("TA", 0, 20, 15, label_visibility="collapsed")

            is_tg= st.toggle("Anti-Gravity Handling", value=False)
            tg_slider= st.slider("TG", 0, 20, 15, label_visibility="collapsed")

with col2:

    with st.container(border=True):

        st.subheader("Mario Kart Combinations")

        col_driver, col_kart, col_tire, col_glider = st.columns(4)

        with col_driver:
            st.image("https://mario.wiki.gallery/images/thumb/4/4a/MK8DX_Funky_Kong_Icon.png/96px-MK8DX_Funky_Kong_Icon.png", caption="Funky Kong")
            st.image("https://mario.wiki.gallery/images/thumb/4/4a/MK8DX_Funky_Kong_Icon.png/96px-MK8DX_Funky_Kong_Icon.png", caption="Funky Kong")
            st.image("https://mario.wiki.gallery/images/thumb/4/4a/MK8DX_Funky_Kong_Icon.png/96px-MK8DX_Funky_Kong_Icon.png", caption="Funky Kong")
            st.image("https://mario.wiki.gallery/images/thumb/4/4a/MK8DX_Funky_Kong_Icon.png/96px-MK8DX_Funky_Kong_Icon.png", caption="Funky Kong")
        
        with col_kart:
            st.image("https://mario.wiki.gallery/images/thumb/e/eb/MK8DX_Inkstriker.png/150px-MK8DX_Inkstriker.png")
            st.image("https://mario.wiki.gallery/images/thumb/e/eb/MK8DX_Inkstriker.png/150px-MK8DX_Inkstriker.png")
            st.image("https://mario.wiki.gallery/images/thumb/e/eb/MK8DX_Inkstriker.png/150px-MK8DX_Inkstriker.png")

        with col_tire:
            st.image("https://mario.wiki.gallery/images/thumb/b/ba/GLATires-MK8.png/150px-GLATires-MK8.png")
            st.image("https://mario.wiki.gallery/images/thumb/b/ba/GLATires-MK8.png/150px-GLATires-MK8.png")
            

        with col_glider:
            st.image("https://mario.wiki.gallery/images/thumb/8/84/Cloud_Glider.png/150px-Cloud_Glider.png")
            st.image("https://mario.wiki.gallery/images/thumb/8/84/Cloud_Glider.png/150px-Cloud_Glider.png")
            st.image("https://mario.wiki.gallery/images/thumb/8/84/Cloud_Glider.png/150px-Cloud_Glider.png")
            st.image("https://mario.wiki.gallery/images/thumb/8/84/Cloud_Glider.png/150px-Cloud_Glider.png")

with col3:

    with st.container(border=True):

        st.subheader("Results")

        variables= ["SL", "SW", "SA", "SG", "AC", "MT", "WG", "IV", "ON", "OF", "TL", "TW", "TA", "TG"]
        values= [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
        df= pd.DataFrame({'Variable': variables, 'Value': values})

        fig= px.bar(df, y='Variable', x='Value', orientation='h', color="Variable", text_auto=True,
                    color_discrete_map={"SL": "dodgerblue", "SW": "dodgerblue", "SA": "dodgerblue", "SG": "dodgerblue", 
                                        "AC": "lightseagreen", "MT": "lightseagreen", "WG": "lightseagreen", "IV": "lightseagreen", 
                                        "ON": "mediumseagreen", "OF": "mediumseagreen", 
                                        "TL": "forestGreen", "TW": "forestGreen", "TA": "forestGreen", "TG": "forestGreen"})
        fig.update_layout(showlegend=False,  margin=dict(l=0,r=0,b=0,t=0), xaxis_title="", yaxis_title="")
        fig.update_xaxes(showticklabels=False)

        st.plotly_chart(fig, use_container_width=True)