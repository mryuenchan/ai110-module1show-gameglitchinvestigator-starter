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

- Which AI tools did you use on this project?
  ChatGPT and the AI coding assistant in VS Code.

- Give one example of an AI suggestion that was correct.
  ChatGPT helped me identify that changing the secret number from an integer to a string could break the comparison between the guess and the secret. I removed that unnecessary conversion. I verified the fix by running the game manually and running pytest.

- Give one example of an AI suggestion that was incorrect or misleading.
  The VS Code AI assistant suggested changes that were more complicated than what I needed, so I did not accept the suggestion exactly as written. I decided to make a smaller and more targeted change because it was easier to understand and verify. I tested my version using pytest and by playing the game manually.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I tested each fix multiple times instead of assuming it worked after changing the code. I ran the live Streamlit game and also used automated tests.

- Describe at least one test you ran and what it showed you about your code.
  I ran `python -m pytest` and all 3 tests passed. The tests checked a correct guess, a guess that was too low, and a guess that was too high. This showed that the main guessing logic and hints worked correctly.

- Did AI help you design or understand any tests? How?
  Yes. AI helped me understand what behavior each test should check and how pytest could verify the expected outcome automatically.

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
