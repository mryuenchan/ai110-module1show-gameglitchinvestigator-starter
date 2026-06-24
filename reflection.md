# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it? It feels just like a regular normal guesser, but the hint is very wrong.
- List at least two concrete bugs you noticed at the start  the hints were not accurate, during the second attempt, I was guided to guess the number 39 but the secret was 8. Another one is that I was forced to end the game saying that I ran out of attempts when I supposedly have 2 left.
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|guess of 50 |Go Higher |Go Lower |None |
|Guess of 25 |Go Higer |Go lower |None |
|Allowed attemps |8 |6 |None |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? 
  ChatGPT
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  It suggested that "if st.session_state.attempts % 2 == 0:" changes the secret from integer to text which makes python compare them in text instead of integer values.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  None. Only the AI agent in VS code was very misleading not ChatGPT
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I had ChatGPT going over the edited code again to make sure it is fixed and I ran the live game 3 more times and made sure that the two bugs are fixed.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code. 
  I ran the live test manually and it worked as expected.
- Did AI help you design or understand any tests? How?
  Yes. I ask ChatGPT to show me what's wrong and why and hints on how to fix what's wrong.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit? 
  Streamlit reruns the whole Python file from top to bottom whenever the user interacts with the app, such as pressing a button or typing into an input box. Session state is like the app’s memory: it keeps important values, such as the secret number, score, attempts, and game status, even after the app reruns. Without session state, the guessing game would create a new secret number every time the player submitted a guess.


---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  Testing habit and prompting strategy. I always test a fix multiple times before I move on to the next bug.
- What is one thing you would do differently next time you work with AI on a coding task?
  I would be more efficient when prompting. I was inefficient this time because I was inexperienced.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  I think AI generated code is very neat and efficient. It is unlike human written code which can be all over the place because of many reasons.
