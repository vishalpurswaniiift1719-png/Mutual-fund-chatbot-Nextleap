# Problem Statement: Mutual Fund FAQ Assistant (Facts-Only Q&A)

---

## Overview

The objective of this project is to build a **facts-only FAQ assistant** for mutual fund schemes, using **Groww** as the reference product context. The assistant will answer objective, verifiable queries related to mutual funds by retrieving information exclusively from official public sources, such as **AMC** (Asset Management Company) websites, **AMFI**, and **SEBI**.

The system must **strictly avoid** providing investment advice, opinions, or recommendations. Every response must include a single, clear source link and adhere to defined constraints around clarity, accuracy, and compliance.

---

## Objective

Design and implement a lightweight **Retrieval-Augmented Generation (RAG)**-based assistant that:

- Answers factual queries about mutual fund schemes
- Uses a curated corpus of official documents
- Provides concise, source-backed responses

---

## Target Users

- **Retail investors** comparing mutual fund schemes
- **Customer support and content teams** handling repetitive mutual fund queries

---

## Scope of Work

### 1. Corpus Definition

We will be selecting the list of all **equity mutual funds by Navi Mutual Fund** for this exercise.

> 🔗 Source: [https://www.indmoney.com/mutual-funds/amc/navi-mutual-fund](https://www.indmoney.com/mutual-funds/amc/navi-mutual-fund)

---

### 2. FAQ Assistant Requirements

The assistant must answer **facts-only queries**, such as:

- Expense ratio of a scheme
- Exit load details
- Minimum SIP amount
- ELSS lock-in period
- Riskometer classification
- Benchmark index
- Process to download statements or capital gains reports

#### Response Constraints

Each response must ensure:

| Constraint | Requirement |
|---|---|
| **Length** | Maximum of **3 sentences** |
| **Citation** | Exactly **one citation link** per response |
| **Footer** | `"Last updated from sources: <date>"` |

#### Category-Aware Disambiguation

The assistant must be able to understand the **category of fund** (Large Cap, Small Cap, Mid Cap, ELSS, etc.) and ask the user which specific fund they want information for if the user only mentions a category or asks a generic question.

> **Example:** If a user asks _"1 yr Returns of large cap fund"_, the chatbot should show the user a list of all large cap funds within the fund house before proceeding to answer.

> [!IMPORTANT]
> **Understand specifics first → Then answer**

---

### 3. Refusal Handling

The assistant must **refuse** non-factual or advisory queries, such as:

- _"Should I invest in this fund?"_
- _"Which fund is better?"_

Refusal responses should:

- Be **polite** and clearly worded
- **Reinforce** the facts-only limitation
- Provide a **relevant educational link** (e.g., AMFI or SEBI resource)

---

### 4. User Interface (Minimal)

The solution should include a simple interface with:

- A **welcome message**
- **Three example questions**
- A visible disclaimer:
  > _"Facts-only. No investment advice."_

---

## Constraints

### 📊 Data and Sources

- Use **only official public sources** (AMC, AMFI, SEBI)
- Do **not** use third-party blogs or aggregator websites

### 🔒 Privacy and Security

Do **not** collect, store, or process:

- PAN or Aadhaar numbers
- Account numbers
- OTPs
- Email addresses or phone numbers

### 🚫 Content Restrictions

- No investment advice or recommendations
- No performance comparisons or return calculations
- For performance-related queries, provide a **link to the official factsheet only**

### ✅ Transparency

- Responses must be **short, factual, and verifiable**
- Every answer must include a **source link** and **last updated date**

---

## Expected Deliverables

### README Document

- Setup instructions
- Selected AMC and schemes
- Architecture overview (RAG approach)
- Known limitations

### Disclaimer Snippet

> _"Facts-only. No investment advice."_

---

## Success Criteria

| # | Criterion |
|---|---|
| 1 | Accurate retrieval of factual mutual fund information |
| 2 | Strict adherence to facts-only responses |
| 3 | Consistent inclusion of valid source citations |
| 4 | Proper refusal of advisory queries |
| 5 | Clean, minimal, and user-friendly interface |

---

## Summary

The goal is to build a **trustworthy, transparent, and compliant** mutual fund FAQ assistant that prioritizes **accuracy over intelligence**. The system should ensure that users receive only verified, source-backed financial information, without any advisory bias or speculative content.
