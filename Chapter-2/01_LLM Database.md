
**What is Vector Database?**

No we won't use SQL, Mongo are any other database when dealing with LLM. Traditinal databases save data but doesn't maintain any relationship between each other. 

Vector databses are used to store the embedded vectors and enable semantic search, So when user queries for any data, It will not return matching text rather it will pull the information related to the given text. 
It stores all related data closely. If you remember when we did Embedding the words close to each other have similar values in vectors. 

---

Similarity Search:

“Similarity search” or “semantic search” refers to finding information that has similar features or meaning from a set of data. It’s like searching for similar movies in an app, looking for similar shoes on an e-commerce website, or finding data related to a specific meaning.

The important aspect of generated embeddings is that similar or semantically related data tend to be located closer to each other, while dissimilar data are located farther apart. This is because AI models are trained on data that helps them identify meanings, similarities, and differences.

<img width="1052" height="495" alt="image" src="https://github.com/user-attachments/assets/9ffae284-4764-4695-8cc1-7a82b9742f20" />

<img width="902" height="907" alt="image" src="https://github.com/user-attachments/assets/6920a1ad-4f92-47ad-bfe2-0c4297e75045" />

Calculating similarity

Now that we understand how data is represented, we can learn how to find relevant results by calculating the distances between the vector representation of the search query and the existing data.

To find potentially similar data vectors to a query vector, we calculate the distance between all data vectors and the query vector.

However, not all data is relevant. Therefore, we only need the data vectors that are closest to the query vector, as they are potentially similar. To improve accuracy, we can limit the number of closest vectors to a certain count. When performing a search, the additional information of count or top “K” is provided, which represents the number of closest vectors.

---

Widely Used Vector Databases:
- Pinecone: Setup, API key generation, index creation, clusters, storing embeddings, similarity search.
- Chroma DB: Installation and basic usage for storing and retrieving embeddings.
- FAISS (Facebook AI Similarity Search): Mentioned as another vector database.
