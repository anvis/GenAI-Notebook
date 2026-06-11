
**What is RAG?**

When we interact with LLM it responds with the data it is trained on and when you want LLM to query on your own data, you provide your documents This is RAG, A Simple RAG.

Instead of forcing the LLM to rely purely on its memory, you hand it a specific data (your domain documents) and say, "Read this page first, and use it to answer my question." This Improves the Accuracy of output.

RAG is Retrieval Augmentation Genreation its Find, Read and Answer. 

Here Retrieval could be anything your app can search the web, read the documents, get data from external databases etc.., Once you got the data you embedd it give it to LLM and you get the answer.

Lets see a basic RAG Pipeline.

- Document Ingestion (Raw data, Remove Noise, Chunk documents)
- Embed with transformer embeddings
- Store in vector DB
- Retrieve top-k chunks
- Pass to LLM for generation

Document Ingestion: 

Whenever we recieve a document we chunk it meaning we break it into multiple pieces, Why we do chunking? Chunking makes retrieval precise and efficient. If you embed the entire document as one vector, retrieval will return the whole thing even if only a small section is relevant. That dilutes precision. Most embedding models will have a token limit.

Fixed Chunking Splits text into chunks of a predetermined size (e.g., 500 tokens, 1,000 characters).

Semantic chunking Splits text based on meaning, structure, or natural boundaries (e.g., paragraphs, sections, headings).

Embedding: 

Convert chunks into dense vector representations using embedding models. We have already learnt about Embedding in Chapter01.

Store in vector DB: 

The Embeddings are stored in Vector Database.

---

Above steps are like pre-requisites from this step the RAG will being.

Now when user sends query, first we check the vector DB with user query and pull out top 2-5 records. And we pass these top-k documents to LLM.

There are different ttechniques involved while storing and retrieving the data from vector DB.




