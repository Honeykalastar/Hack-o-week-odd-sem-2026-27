# Week 5 & 6 Activity

## Neural Network Math Playground

### Project Objective

The objective of this project is to understand and demonstrate the mathematical concepts used in Artificial Intelligence and Neural Networks through an interactive web application.

The project focuses on two major areas:

* **Linear Algebra:** Vectors, Matrices, Dot Product and Eigenvalues
* **Calculus:** Derivatives, Gradients and Chain Rule

These concepts are further connected to **Backpropagation**, which is one of the fundamental learning mechanisms used in neural networks.

---

## Week 5 — Linear Algebra and Project Development

### Activities Completed

During Week 5, the focus was on understanding the basic linear algebra concepts required for neural networks and implementing them in the project.

### 1. Vectors

Implemented vector operations including:

* Vector addition
* Vector subtraction
* Vector magnitude
* Dot product

Vectors were represented as numerical arrays and processed using Python and NumPy.

### 2. Dot Product

Implemented the dot product of two vectors.

The dot product was used to demonstrate how input values and weights can be combined, which is an important operation inside a neural network.

### 3. Matrices

Implemented basic matrix operations including:

* Matrix addition
* Matrix multiplication
* Matrix-vector multiplication
* Determinant calculation

These operations demonstrate how data can be transformed using matrices.

### 4. Eigenvalues — Intuition

An intuition-level demonstration of eigenvalues and eigenvectors was added.

The project explains that an eigenvector is a special direction that remains on the same line after a matrix transformation, while the eigenvalue represents the scaling factor.

### 5. Backend Development

A Python Flask backend was created to perform the mathematical calculations.

The backend contains separate modules for:

* Vector operations
* Matrix operations
* Calculus operations
* Neural network calculations

---

## Week 6 — Calculus and Backpropagation

### Activities Completed

During Week 6, the focus was on calculus concepts and their connection with neural network learning.

### 1. Derivatives

Implemented a derivative demonstration using a simple mathematical function.

The application calculates the slope of the function at a selected value of `x`.

This demonstrates how derivatives describe the rate at which a function changes.

### 2. Gradients

Implemented a two-variable gradient example.

The gradient shows the direction and rate of the steepest increase of a function.

This helps explain how neural networks determine how their parameters should change during learning.

### 3. Chain Rule

Implemented an educational demonstration of the chain rule.

The project demonstrates how derivatives of multiple functions can be combined:

**dy/dx = (dy/dz) × (dz/dx)**

The chain rule is important because neural networks contain multiple connected operations and layers.

### 4. Backpropagation Demonstration

A small neural network was implemented to demonstrate the basic idea of backpropagation.

The demonstration contains:

**Input → Hidden Neuron → Output**

The application performs:

1. Forward propagation
2. Output calculation
3. Error calculation
4. Derivative calculation
5. Gradient calculation
6. Weight update

This demonstrates how the chain rule is used to calculate gradients and adjust neural network weights.

### 5. Frontend Development

An interactive frontend was developed using:

* HTML
* CSS
* JavaScript

The interface provides separate sections for linear algebra, calculus and backpropagation.

---

## Technologies Used

* **Python** — Mathematical calculations and backend
* **Flask** — Backend web framework
* **NumPy** — Vector and matrix operations
* **SymPy** — Derivative and gradient calculations
* **HTML** — Application structure
* **CSS** — User interface design
* **JavaScript** — Interactive frontend and API communication

---

## Project Workflow

The overall learning workflow of the project is:

**Vectors → Matrices → Dot Product → Eigenvalues → Derivatives → Gradients → Chain Rule → Backpropagation**

This shows how fundamental mathematical concepts are connected to the learning process of neural networks.

---

## Learning Outcomes

By completing Week 5 and Week 6, the following concepts were understood and implemented:

* Representation of data using vectors and matrices
* Vector and matrix operations
* Understanding of dot products
* Intuition behind eigenvalues and eigenvectors
* Understanding derivatives as rates of change
* Understanding gradients
* Understanding the chain rule
* Basic understanding of backpropagation
* Connecting mathematics with neural network learning
* Developing a Python Flask-based mathematical web application

---

## Final Outcome

The final result is an interactive **Neural Network Math Playground** that allows users to experiment with mathematical concepts instead of only reading theoretical definitions.

The project demonstrates how **Linear Algebra and Calculus form the mathematical foundation of Neural Networks and Machine Learning.**
