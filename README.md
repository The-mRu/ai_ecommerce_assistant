# AI E-Commerce Assistant

An AI-powered e-commerce backend assistant built using FastAPI, MongoDB, and OpenAI SDK.

This project demonstrates how to build a real-world AI shopping assistant with:
- product search
- product comparison
- review summarization
- recommendation system
- conversational memory
- multi-user chat support
- AI orchestration using OpenAI SDK

---

# Features

## User Features

### AI Chat Assistant
- Conversational shopping assistant
- Multi-user memory support
- Last 10 messages remembered

### Product Search
Examples:
- "Show gaming phones"
- "Any mobile under 700"
- "Budget friendly smartphones"

### Product Comparison
Examples:
- "Compare iPhone 15 and Samsung S24"
- "Which is better for gaming?"

### AI Recommendations
Examples:
- "Best gaming beast under 700"
- "Suggest me a budget phone"

### Review-Aware Responses
- Uses customer reviews during comparison
- Prioritizes latest reviews

---

# Tech Stack

- Python
- FastAPI
- MongoDB
- OpenAI SDK
- PyMongo

---

# Project Structure

```bash
ai_ecommerce_assistant/

│
├── main.py
│
├── database/
│   ├── mongodb.py
│   ├── insert_products.py
│   ├── insert_users.py
│   ├── insert_reviews.py
│   └── insert_orders.py
│
├── services/
│   ├── ai_service.py
│   ├── tools.py
│   └── prompts.py
│
├── .env
├── requirements.txt
└── README.md
````

---

# Database Collections

## products

Stores product information.

Example fields:

* name
* category
* sub_category
* price
* battery
* camera
* gaming
* tags
* rating

---

## reviews

Stores product reviews.

Example fields:

* product_name
* user
* review
* rating
* created_at

---

## users

Stores user information.

---

## orders

Stores order data.

---

## chat_history

Stores conversational memory for users.

---

# Setup Instructions

## 1. Clone Project

```bash
git clone <your_repo_url>
cd ai_ecommerce_assistant
```

---

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

### Windows

```bash
.venv\Scripts\activate
```

### Mac/Linux

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
MONGODB_URI=mongodb://localhost:27017
```

---

# MongoDB Setup

Make sure MongoDB is running locally.

Default database:

```text
ai_ecommerce
```

---

# Insert Sample Data

## Products

```bash
python -m database.insert_products
```

## Users

```bash
python -m database.insert_users
```

## Reviews

```bash
python -m database.insert_reviews
```

## Orders

```bash
python -m database.insert_orders
```

---

# Run Server

```bash
uvicorn main:app --reload
```

Server:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

# Example Requests

## Product Search

```json
{
  "user_id": "rayhan",
  "message": "Show gaming phones"
}
```

---

## Product Comparison

```json
{
  "user_id": "rayhan",
  "message": "Compare iPhone 15 and Samsung S24"
}
```

---

## Recommendations

```json
{
  "user_id": "rayhan",
  "message": "Best gaming beast under 700"
}
```

---

# AI Architecture

## Workflow

```text
User Message
      ↓
Intent Extraction
      ↓
Backend Orchestration
      ↓
MongoDB Retrieval
      ↓
AI Response Generation
      ↓
User
```

---

# Concepts Implemented

* AI Tool Calling
* Conversational Memory
* Multi-user Chat System
* Structured Intent Extraction
* Backend Orchestration
* Recommendation Logic
* Review Summarization
* MongoDB Integration
* Semantic Query Normalization

---

# Future Improvements

* RAG Integration
* Vector Search
* Embeddings
* Admin AI Dashboard
* Async Processing
* Streaming Responses
* Recommendation Ranking
* Personalized User Profiles

---

# Learning Outcomes

This project demonstrates practical understanding of:

* OpenAI SDK
* AI backend architecture
* AI orchestration
* Retrieval workflows
* Conversational systems
* Database-driven AI systems

---

# Author

Md Rayhan Uddain 

&&

 ChatGpt
```
```
