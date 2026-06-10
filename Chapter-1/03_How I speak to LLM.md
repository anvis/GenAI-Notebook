
**Prompt Engineering**

Your prompts define the LLM’s behavior, A small change in phrasing can significantly alter the output — making prompt design both powerful and delicate.

Note Prompt is not always what user sends, If we have a application we take user query and follow one of the prompting technique internally and send that enhanced prompt to Model.

It is just a way we talk to a model, but we should be careful think of example it has too much of data and you have asked a query it will try to answer you in a generic way. But if you tell the model what are you asking for and to whom you are asking(Role) and the usage by setting the tone you will get the answer you need.

There are many methods defined and they will evolve day by day. few are below.
- Instruction based
- Role based
- Few short : A collection of examples, stored in a vector store Retrieved Combined to user query and sent to LLM.
- Zero-Short : No example
- One short : Single example
- Chain of Thoughts : Break down complex tasks into smaller, logical steps.
- Structured output format : Extract information in Json format
- COSTAR framework

---

C – Context:: Provide background or situation.

O – Objective:: State the goal or task

S – Style:: Define tone, format, or persona

T – Tone:: Emotional or communicative flavor

A – Audience:: Specify who the output is for

R – Response:: Indicate the expected format

---

