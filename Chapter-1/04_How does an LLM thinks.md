
**How does an LLM thinks?**

In reality, an LLM doesn't "think" the way humans do.

It doesn't know why the answer is correct;

It calculates the probability of certain words appearing near other words.

---

Before a model can process a prompt, it has to learn how language works. 
During its training phase, the model reads billions of pages of text (books, articles, websites).

Instead of learning facts or concepts like a human student, it analyzes **how words relate to each other**. 

---

The core "thinking" happens inside a neural network architecture called a **Transformer**. 
The defining feature of this architecture is a mechanism called **Attention** (specifically, Self-Attention).

As the model processes your prompt, the attention mechanism looks at every token in relation to every other token. 
It decides which words are most important to the overall meaning.

Once the model understands the mathematical context of your prompt, it begins to generate a response. 
Crucially, it writes its answer one token at a time.
