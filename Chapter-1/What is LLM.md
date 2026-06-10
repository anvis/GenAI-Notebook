
**What is LLM?**

LLM is Large Language Model, It is a model that is large and understand human language. Yes it is a model that acts on Input and provides you an Output. And when I say it is large it is trained on large data the model is trained on large data and Now this model can understand the Human Language.

---

**How LLM understands Human Language?**

When User sends a prompt to LLM, Here prompt is a plain english language which is human language. This prompt, the english text is converted to Numerics representing Numbers. So the words are converted into numerics this process is called encoding.

In Encoding each word is represted by Zeros and ones.

**1. One-Hot Encoded Vector** : - Only one position in the vector is set to **1**, while all others are **0**.

#### **Example:**
If we have a vocabulary of 4 words: `["cat", "dog", "fish", "bird"]`, their one-hot vectors would be:

```
cat   → [1, 0, 0, 0]
dog   → [0, 1, 0, 0]
fish  → [0, 0, 1, 0]
bird  → [0, 0, 0, 1]
```

The problem with encoding is each word is not related to one other, The encoding doesn't always represent a word in same manner the cat may not produce same numerics in every sentence.

---

**Embeddings**

The Solution is Embeddings, where it captures meaning of each word. Embeddings are two levels word level and Sentence level.

#### **Example:**

If word embeddings have 3 dimensions:
```
cat   → [0.85, 0.12, -0.42]
dog   → [0.88, 0.14, -0.39]
fish  → [0.30, 0.60, -0.10]
```
Notice that "cat" and "dog" have similar values because they are semantically related.

Word level Algorithms: Word2Vec, GloVe

What are Sentence Transformers? 

Sentence Transformers are a Python framework that makes it easy to generate high-quality embeddings for sentences, paragraphs, or entire documents, enabling tasks like semantic search, clustering, and similarity comparison.

Sentence level Algorithms: BERT, GPT

Example:

Query: “bank” 
Word2Vec/GloVe: Same vector for “river bank” and “bank account.” 
Sentence Transformers: Different embeddings because the surrounding sentence changes meaning. 

---

**Tokenization**

Neural networks operate on fixed-size numerical vectors, not raw text. Tokenization converts variable-length text into a sequence of integers (token IDs), which are then mapped to embedding vectors the model can actually process mathematically.

When you speak with LLM it doesn't remember everything you type in, it has some memory, It is called **context window**. If your text is more than this context window your LLM will forget the context. So we 
