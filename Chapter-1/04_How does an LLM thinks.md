
**How does an LLM thinks?**

In reality, an LLM doesn't "think" the way humans do.

It doesn't know why the answer is correct;

It calculates the probability of certain words appearing near other words.

---

Before a model can process a prompt, it has to learn how language works. 
During its training phase, the model reads billions of pages of text (books, articles, websites).
Instead of learning facts or concepts like a human student, it analyzes **how words relate to each other**. 

---

Based on Embeddings Vectors it adjusts it weights and bias in Neural Network so everytime user asks a prompt it can generate next token. Most of the time the weights are static.

---

The core "thinking" happens inside a neural network architecture called a **Transformer**. 
The defining feature of this architecture is a mechanism called **Attention** (specifically, Self-Attention).

As the model processes your prompt, the attention mechanism looks at every token in relation to every other token. 
It decides which words are most important to the overall meaning.

Once the model understands the mathematical context of your prompt, it begins to generate a response. 
Crucially, it writes its answer one token at a time.

Some models are trained using Reinforcement Learning to generate an internal "chain of thought" before giving you the final answer. To test and analyze the response.

---

When you chat with an LLM, you are using it in Inference mode.

During inference, the billions of weights and biases inside the neural network are completely static (frozen). They do not change by even a fraction of a percent based on what you type. If you ask the model a question, and then ask it the exact same question a minute later, it uses the identical mathematical network both times.

If weights don't change, how does it understand context?

It does this through activation states and the Attention Mechanism, not by changing weights.

Think of the neural network like a massive, complex musical instrument, The Weights: These are the physical pipes and keys and Your Query: This is the sheet music you feed into it. 

The Attention Mechanism allows the tokens in your prompt to mathematically influence how the signals flow through those fixed weights.

---

**The LLM's "brain" is mathematically locked in place when you talk to it. It adapts to you not by changing its structure, but by routing your prompt through its incredibly vast, pre-existing maze of mathematical pathways.**
