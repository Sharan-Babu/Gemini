import streamlit as st
import streamlit.components.v1 as components
import pickle


st.title('Gemini 👥')
st.caption('Eclectic News Search Engine')

with open('anchor_vertices_list','rb') as file:
    anchor_vertices_list = pickle.load(file)

with open('children_news_info','rb') as file:
    children_news_info = pickle.load(file)    

#st.write(anchor_vertices_list)
#st.write(children_news_info)

# Create 2 columns view
st.markdown("# Anchor News")


#components.iframe("https://thealtworld.com/paul_craig_roberts/west-vs-russia-reaching-point-of-no-return",scrolling=True,height=500)

for i,article in enumerate(anchor_vertices_list):
	link = article['link']
	media = article['media']
	rank = article['rank']
	summary = article['summary']
	title = article['title']
	children = article['children']

	st.subheader(f"{i+1}. {title}")
	st.write(f"News Link: {link}")
	st.image(media,caption="News Thumbnail")
	st.markdown("#### Summary")
	st.write(summary)
	
	if len(children)>0:
		st.markdown("**Related Articles (ID)**:")
		for related_article in children:
			#st.markdown(f": ")
			st.markdown(f"**{children_news_info[related_article]['title']}**: {related_article}")

	st.write("")
	st.write("")	
	st.markdown("<hr>",unsafe_allow_html=True)


st.title("Search Related News")
related_news_id = st.text_input("News ID","8ee07b4cdb24bf72d877bb0834132495")
st.write("")

if st.button("Search"):
	st.write("")
	st.write("")
	article = children_news_info[related_news_id]
	link = article['link']
	media = article['media']
	rank = article['rank']
	summary = article['summary']
	title = article['title']

	st.subheader(f"{title}")
	st.write(f"News Link: {link}")
	st.image(media)
	st.markdown("#### Summary")
	st.write(summary)