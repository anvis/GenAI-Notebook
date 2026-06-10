
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

Embeddings (Vectors): Each token is converted into a long string of numbers (a vector). These numbers place the token into a multi-dimensional mathematical space. Words with similar meanings or contexts (like "king" and "queen", or "coffee" and "tea") are placed close together in this digital space.

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

**Tokenization** — Breaking Text into Pieces

Before any learning happens, text is split into tokens.

"understanding" → ["under", "stand", "ing"]
"GPT" → ["G", "PT"]

Whatever Text we give to LLM first converted into Tokens, Tokenization is nothing but breaking the given text. 
It can break on word level, sentence level or character level. 
After breaking the text it assigns Id to each token (token IDs), which are then mapped to embedding vectors the model can actually process mathematically.

- Step 1: Divide the Input Text into Tokens 
- Step 2: Assign an ID to Each Token

Algorithms : Byte Pair Encoding (BPE)

Frequent words are merged and have less tokens, where as rare words are splitted so we have more tokens.

Let’s take your two words:

1️⃣ "hello"

Common word, appears frequently in training data.
During BPE training, the sequence h, e, l, l, o gets merged repeatedly because "hello" occurs so often.
Eventually, "hello" becomes a single token in the tokenizer’s vocabulary.

2️⃣ "antidisestablishmentarianism"

Rare word, appears very few times in training data.
The tokenizer hasn’t seen it enough to merge all its sub-parts.
So it breaks it into smaller known subword tokens like:
["anti", "dis", "establish", "ment", "arian", "ism"]
Each of these subwords is a token, so the word becomes 6 tokens.

---

**Self-attention** lets every token look at every other token and ask: "how relevant are you to understanding me?" This produces context-aware representations — the same word gets a different vector depending on its surroundings.

**Multiple attention heads** capture different types of relationships simultaneously (syntactic, semantic, coreference, etc.).

---

**Context Window**

When you speak with LLM it doesn't remember everything you type in, it has some memory, It is called **context window**. If your text is more than this context window your LLM will forget the context.

A larger context window enables an AI model to process longer inputs and incorporate a greater amount of information into each output.
