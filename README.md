# Collatz Scribbles

An interactive web application to explore the mathematical magic of the Collatz Conjecture by visualizing the Collatz sequence for any number between 1 and 10,000.

## What is the Collatz Conjecture?

The Collatz Conjecture is one of the most famous unsolved problems in mathematics. Despite its simple rules, no one has been able to prove it works for all numbers.

**The rules are:**
- If the number is **odd**: multiply by 3 and add 1 → `3n + 1`
- If the number is **even**: divide by 2 → `n / 2`

The conjecture states that no matter what positive integer you start with, you'll always eventually reach 1.

## Features

- 🔢 Generate Collatz sequences for any number from 1 to 10,000
- 📊 Interactive graph visualization of the sequence
- 🎨 Clean, intuitive user interface

## Project Structure
```
├── index.html                    # Landing page/interface
├── Collatz.py                    # Collatz sequence computation
├── Graph_Structure.py            # Graph node positioning logic
├── Collatz_Sequence_Graph.py     # Graph visualization generation
└── app.py                        # Flask backend server
```


## Technologies Used

- **Python**: Backend logic
- **Flask**: Web framework
- **PyVis**: Interactive network visualization
- **NetworkX**: Graph data structures and algorithms




