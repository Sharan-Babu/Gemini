# Gemini 👥
An eclectic news search engine that helps with deduplication of news articles and enriches your reading experience.

**Contributers and Contact Information: [Sharan Babu, sharanbabu2001@gmail.com / 19211a05q9@bvrit.ac.in, www.sharanbabu.ml ]**

**Problem Statement addressed : [Reduce The Noise Of News Search (No.7) ]**

**Description**: 

Time is of essence and hence spending it by only consuming necessary information is very important. That is the problem this project tries to solve in the domain of news search. **Gemini** is an eclectic news search engine that helps with deduplication of news articles and enriches your reading experience. Enables readers to dig deep into a certain opinion or explore multiple facets of the news at hand.

**Submission Video** : [Link](https://www.youtube.com/watch?v=w9tYn8WQJzk)  

**Current Solution Export**: [Link](https://github.com/Sharan-Babu/Gemini/blob/main/export_576836961.tar.gz)

**Fun Fact**: '_Gemini_' is synonymous to the word '_clone_' or '_twin_' and hence I thought it would be a cool play on the word for a project that dealt with deduplication.
				

## Impactfulness
Productivity and value for time is ever-so important in today's fast moving world. We are constantly in search for tools that bolster this notion without sometimes realizing that we might be sacrificing something important in the process. Take 'News Search' as a problem for example. As an end consumer, we want quick access to happenings around the world and this requirement is readily fulfilled by the mobiles in our pocket, but in the quest for this speed, are we getting an entire picture of the event (news) at hand? **Probably not**. That is where **Gemini** comes in. Gemini with the power of Graph Technology is able to provide meaningful and otherwise looked-over insights that can totally change your viewpoint on a matter. With Gemini, you can not only save a lot of time by ensuring that you are not reading the same content over and over again but also answer interesting questions like:
- Which countries have what opinion about an event?
- Inherent bias in the subject matter being discussed
- How two entities (like countries) are related to an event?
- Connection of keywords and topics to news from different sources
- Centrality of a particular opinion?

and many such insightful questions. The revelations are often eye-opening and help lead to healthy conclusions.

## Innovative use case of graph
Use of a hyper-node based schema where the hyper-nodes lead to related children nodes and the hyper-nodes (called 'ANCHOR NEWS' in the context of this project) themselves are linked to each other with a semantic similarity score provides an innovative and unique way to model the problem of news deduplication in such a way that deduplication is inherent and the defined schema allows for a wide range of custom queries to be implemented for obtaining varied and meaningful insights in an optimal way. Schema is easily extendable to add new properties/attributes for news articles.

The way the graph has been modelled allows for it to be extended for non-news use cases as well. It is magic when you are able to explore the populated graph in a Graph Studio or visualization tool of your choice. The connections induce new ideas as to how the graph can be queried in creative ways to mine new patterns.

## Ambitiousness
**Gemini** is trying to solve a _pressing_ and _ever-existent_ problem. This project has the potential to help people form _concerted and unbiased_ opinions thereby leading to a safe and just society. **Gemini** is highly scalable and generalizable as well.

**Schema**:

![schema](https://user-images.githubusercontent.com/50396375/164199743-fdc2f3d4-8ea0-40d1-aa07-0f0806bb9811.PNG)


## Applicability
**Gemini 👥** helps address a lot of use cases and its easy schema extensibility makes it convenient and simple to _add new dynamics_ to the existing graph.
Examples of use cases:
- Normal user browsing a news topic
- Organization checking public reception of it's fresh developments on news
- Organization checking how it's competitors are performing in the eyes of the public sphere
- Empathetic understanding of the problem
- Exploratory analysis (eclectic surfing) & subject-matter deep dive (related news drill-down)


Other additions: 

 - **Data**: Initial data fetched from https://newscatcherapi.com/ and later enriched (metadata creation) using different NLP models.
 - **Technology Stack**: Python, TigerGraph, Dataframe Processing, Semantic Search, Sentiment Analysis, Keyword Generation, Website (Streamlit)
 - **Visuals/Project Images**: [Link](https://github.com/Sharan-Babu/Gemini/tree/main/images)
 - **Project Link**: [Link](https://colab.research.google.com/drive/1-ebU3UMTEEK21HfflGEwQWnQgmAu8vix?usp=sharing)

## Dependencies

This project was built using Python. Required libraries can be found in the **requirements.txt** file of this repository.

## Installation

1. Open this [Google Colab Link](https://colab.research.google.com/drive/1-ebU3UMTEEK21HfflGEwQWnQgmAu8vix?usp=sharing) or download the **Gemini.ipynb** file from this repository and open it using a Jupyter Notebook (You can also simply open the Gemini.ipynb file in Github itself and click on the 'Open in Colab' badge at the top). Data is fetched from _newscatcher API_ and I have hardcoded my API key. You can use the same while executing or get your own at https://app.newscatcherapi.com/auth/register .

2. Simply, execute all the cells in the Colaboratory notebook in order. Each cell is documented as to what purpose it serves and the time of execution if it takes a while to execute. There are only 3 cells in the entire notebook whose values are to be changed. Those are:

2a. Enter your preferred news search term in this cell before executing.

  ![s1](https://user-images.githubusercontent.com/50396375/164226269-dcf88bbe-5247-4728-919b-560a9abc7068.PNG)

2b. In this cell, we establish a connection to our TigerGraph instance. So, create an instance with Blank Started Kit and replace the connection paramters & credentials in this cell with yours.

  ![TigerGraph Dashboard](https://user-images.githubusercontent.com/50396375/164228960-6fa6dc5f-1cc9-4016-88da-cb01420a12e6.PNG)

  ![s2](https://user-images.githubusercontent.com/50396375/164226469-9e093343-f0f4-4b7d-8032-4db42bf0911b.PNG)

2c. The following cell requires no change if the above 2 cells were changed accordingly.

  ![s3](https://user-images.githubusercontent.com/50396375/164226882-6016a194-d920-4155-a5eb-7c15700173a1.PNG)

3. All the other cells can be executed as it is. The Colab notebook has been structured in such a way that the flow through it is smooth for the person running it and each component of this project has been separately executed with an example for better understanding of how the project was built.

4. If you used the Colab notebook for execution, Download the files called **anchor_vertices_list** and **children_news_info** from the left pane.
  
  ![s4](https://user-images.githubusercontent.com/50396375/164228093-0e54e762-959e-458c-8633-1cb557dc0084.PNG)  

5. Clone this repository.
~~~
git clone https://github.com/Sharan-Babu/Gemini.git
~~~

6. Ensure that you have the files **anchor_vertices**, **children_news_info** and **gemini.py** in the same folder. If you had changed the search term, replace the **anchor_vertices** and **children_news_info** files in the cloned repository with the ones you downloaded in step 4. Now, we are ready to spin up the website.

7. Install streamlit
~~~
pip install streamlit
~~~

8. Run the Web Application
~~~
streamlit run gemini.py
~~~

9. You can now view the website. You can also visit your instances' GraphStudio to view all the populated data and explore the graph.
  
  ![website pic2](https://user-images.githubusercontent.com/50396375/164228873-1120e8d1-b5ed-4447-9a89-eda007824d0d.PNG)
  
  ![all_paths_finding](https://user-images.githubusercontent.com/50396375/164229046-4b3b6215-1e65-46e9-86a2-1bc09ef13a50.PNG)
  
  ![anchor_news_info](https://user-images.githubusercontent.com/50396375/164229063-2267181c-a1f5-48b4-b9e3-559b956a8a3a.PNG)





## Future Improvements

The solution and the way it has been built can be extended into a regular search engine capable of generalizing on regular websites (non-news) as well; for different search terms.

## Reflections

Explored and used Graph technology for the first time and it was a very fulfilling experience. Learned about how existing news search engines work, their strengths and weaknesses and how cutting edge advances in NLP (keyword generation, semantic search) can be used to make news search better for the readers.

_How it was built_?
- Fetched news articles from newsapicatcher.com. Used the PyTigerGraph Python library to interact with the TigerGraph instance. 
- Used 3 different NLP models for Semantic Search, Keyword Generation and Sentiment Analysis respectively. Helps with enriching the news articles with additional metadata. 
- Later, loaded all data to the TigerGraph instance and processed/explored data in several ways using custom GSQL queries as well as special algorithms like centrality and similarity. 
- Finally, results are shown to the end-user in a Streamlit web application.



**Link to my TigerGraph notes**: https://github.com/Sharan-Babu/Gemini/blob/main/TigerGraph%20Notes.pdf

**Helpful Code Snippets for learning TigerGraph**: https://github.com/Sharan-Babu/Gemini/tree/main/code_snippets

**Useful Reference Links**:
1) https://docs.tigergraph.com/cloud/start/overview
2) https://www.tigergraph.com/graphstudio/
3) https://docs.tigergraph.com/graph-ml/current/intro/
4) https://colab.research.google.com/drive/1JhYcnGVWT51KswcXZzyPzKqCoPP5htcC
5) https://pytigergraph.github.io/pyTigerGraph/
6) https://docs.tigergraph.com/tigergraph-server/current/api/built-in-endpoints#_upsert_data_to_graph
7) https://newscatcherapi.com/
8) https://github.com/MaartenGr/KeyBERT
9) https://graphforall.devpost.com/details/inspiration#h_1353131838381643228912926

Special thanks to **Ashleigh Faith** for the great problem statement, detailed description and attached resources.
