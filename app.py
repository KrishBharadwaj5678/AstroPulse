import streamlit as st
import requests
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="Free Online Horoscope",
    page_icon="icon.png",
    menu_items={
        "About":"Stay updated with daily,weekly and monthly horoscopes tailored to your zodiac sign. Align yourself with the cosmic rhythms for better living."
    }
)

st.write("<h2 style='color:#FFC107;'>Your Future with Celestial Insights.</h2>",unsafe_allow_html=True)

with st.expander("What Each Zodiac Sign Represents?"):
    st.write("""<ol><li>Aries (मेष) - Aries are natural leaders who are passionate and enthusiastic about new ventures.</li>
             <li>Taurus (वृषभ) - Taureans are known for their stability, determination, and appreciation for the finer things in life.</li>
             <li>Gemini (मिथुन) - Geminis are versatile and enjoy intellectual stimulation and social interaction.</li>
             <li>Cancer (कर्क) - Cancers are deeply intuitive and value home and family.</li>
             <li>Leo (सिंह) - Leos have a strong presence and love to be in the spotlight.</li>
             <li>Virgo (कन्या) - Virgos are detail-oriented and strive for perfection in their endeavors.</li>
             <li>Libra (तुला) - Libras value balance and harmony in relationships and their surroundings.</li>
             <li>Scorpio (वृश्चिक) - Scorpios are known for their depth of emotions and their ability to transform and regenerate.</li>
             <li>Sagittarius (धनु) - Sagittarians are explorers who seek knowledge and new experiences.</li>
             <li>Capricorn (मकर) - Capricorns are determined and work hard to achieve their long-term goals.</li>
             <li>Aquarius (कुंभ) - Aquarians are forward-thinking and value individuality and progressive ideas.</li>
             <li>Pisces (मीन) - Pisceans are empathetic and have a strong connection to their inner world and the emotional needs of others.</li></ol>""",unsafe_allow_html=True)

sign=st.selectbox("Select your sign",["Aries ♈","Aquarius ♒","Taurus ♉","Gemini ♊","Cancer ♋","Leo ♌","Virgo ♍","Libra ♎","Scorpio ♏","Sagittarius ♐","Capricorn ♑","Pisces ♓"])

time=st.radio("Select Horoscope Duration",["Monthly","Weekly","Daily"])
if time=="Daily":
    day=st.radio("Select Your Day",["Today","Yesterday","Tomorrow"])

language=st.radio("Choose Your Language",["English","Hindi"])
btn=st.button("Get Horoscope")
if btn:
    try:
        new_sign=sign.split(" ")[0]
        if language=="English":
                target="en"
        else:
                target="hi"

        def horoscope_data(data):
            astro_insights=GoogleTranslator(target=target).translate("Horoscope Details")
            with st.expander(f"{astro_insights}"):
                astro_data = GoogleTranslator(target=target).translate(data["data"]["horoscope_data"])
                st.write(f"<h2 style=font-size:20px;color:#FFA500;line-height:34px;>{astro_data}</h2>",unsafe_allow_html=True)
        
        def Call_API(api_endpoint,day):
            url = f"https://horoscope19.p.rapidapi.com/get-horoscope/{api_endpoint}"
            querystring = {"sign":new_sign,"day":day}
            headers = {
                    "x-rapidapi-key": "c0e897e06bmshf1b07b02427bc79p1edb79jsn0132d0db5ef9",
                    "x-rapidapi-host": "horoscope19.p.rapidapi.com"
            }
            response = requests.get(url, headers=headers, params=querystring)
            return response.json()
        
        def Monthly_Data(translate,colorcode,fontsize):
            data= GoogleTranslator(target=target).translate(f"{translate}")
            st.write(f"<h2 style=color:{colorcode};font-size:{fontsize};>{data}</h2>",unsafe_allow_html=True)

        def week_daily(translate):
            data=GoogleTranslator(target=target).translate(translate)
            st.write(f"<h2 style=color:#00BFFF;font-size:30px;>{data}</h2>",unsafe_allow_html=True)

        if(time=="Monthly"):
            monthly_data=Call_API("monthly",None)
            horoscope_data(monthly_data)
            Monthly_Data(f"Challenging Days: {monthly_data['data']['challenging_days']}", "#e31e1e", "32px")
            Monthly_Data(f"Favorable Days: {monthly_data['data']['standout_days']}", "#32CD32", "33px")
            Monthly_Data(f"Month: {monthly_data['data']['month']}", "#00BFFF", "33px")
            
        elif(time=="Weekly"):
            weekly_data=Call_API("weekly",None)
            horoscope_data(weekly_data)
            week_daily(f"Week: {weekly_data['data']['week']}")
        
        elif(time=="Daily"):          
            daily_data=Call_API("daily",day.upper())
            horoscope_data(daily_data)
            week_daily(f"Date: {daily_data['data']['date']}")
    except:
         st.error("Network Error 🔌")
