# Q2 – AI Based Travel Planner Using Domain Knowledge Bases

## Problem Statement

Design and implement an AI-based Travel Planner that reuses existing domain knowledge bases such as tourist destinations, food recommendations, travel preferences, personalized tour plans, and cost assessment to assist users in planning trips based on their interests and budget constraints.

---

## Approach

This project implements an intelligent travel planning system that uses multiple domain-specific knowledge bases to generate personalized travel recommendations.

The system collects user preferences such as:

* Travel interest
* Budget category
* Trip duration

Based on this information, the planner analyzes the available knowledge bases and recommends suitable destinations along with attractions, food suggestions, travel essentials, itinerary generation, and estimated expenses.

The implementation combines knowledge representation with rule-based decision making to simulate an AI-assisted travel recommendation system.

---

## Knowledge Bases Used

The travel planner reuses multiple domain knowledge bases.

### 1. Destination Knowledge Base

Stores information about tourist destinations including:

* Travel categories
* Budget suitability
* Tourist attractions
* Activities available

Examples:

* Goa
* Manali
* Jaipur
* Kerala
* Ladakh

### 2. Food Recommendation Knowledge Base

Each destination contains regional food recommendations.

Examples:

* Goan Curry
* Seafood Platter
* Himachali Thali
* Dal Baati
* Kerala Fish Curry
* Thukpa

### 3. Travel Essentials Knowledge Base

Provides recommendations based on travel interests.

Examples:

* Trekking shoes for mountain trips
* Sunscreen for beach destinations
* Safety equipment for adventure travel
* Guidebooks for historical tours

### 4. Cost Assessment Knowledge Base

Stores estimated costs for:

* Accommodation
* Food
* Transportation

The planner uses this information to estimate the overall travel budget.

---

## AI Recommendation Strategy

The system uses a scoring-based recommendation approach.

### Interest Matching

Destinations that match the user's preferred travel style receive higher scores.

Examples:

* Beach lovers receive Goa recommendations.
* Adventure travelers receive Manali or Ladakh recommendations.
* History enthusiasts receive Jaipur recommendations.

### Budget Matching

The planner compares the user's budget category with destination affordability.

* Low Budget
* Medium Budget
* High Budget

Destinations that satisfy budget requirements receive additional priority.

### Ranking

All destinations are scored and ranked.

The highest-ranked destinations are displayed as personalized recommendations.

---

## Features

### Personalized Destination Recommendation

Generates destination suggestions based on:

* User interests
* Budget preferences

### Tourist Attraction Recommendation

Displays major attractions available at the selected destination.

### Food Recommendation

Suggests local cuisine associated with the destination.

### Travel Essentials Recommendation

Provides packing suggestions and travel preparation advice.

### Personalized Tour Plan

Automatically generates a day-wise itinerary using available activities.

### Cost Assessment

Calculates estimated expenses including:

* Accommodation cost
* Food cost
* Transportation cost
* Total trip cost

### Smart Travel Suggestions

Provides destination-specific travel insights and recommendations.

---

## Files

| File                | Description                                                                                     |
| ------------------- | ----------------------------------------------------------------------------------------------- |
| `travel_planner.py` | AI-based travel planner using domain knowledge bases and personalized recommendation techniques |

---

## Setup

Run the program:

```bash
python travel_planner.py
```

---

## Running the Program

The user is prompted to enter:

1. Name
2. Travel Interest
3. Budget Category
4. Number of Travel Days

Example interaction:

```text
Enter your name: Sushanth
Enter your interest: adventure
Enter your budget: medium
Enter number of travel days: 5
```

The system then:

1. Recommends suitable destinations.
2. Displays tourist attractions.
3. Suggests local food options.
4. Recommends travel essentials.
5. Generates a personalized itinerary.
6. Performs cost assessment.
7. Provides AI-based travel suggestions.

---

## Example Output

```text
Recommended Destinations

1. Manali
2. Ladakh

Select destination number: 1

PERSONALIZED TOUR PLAN

Traveler      : Sushanth
Destination   : Manali
Duration      : 5 Days

Tourist Attractions
• Solang Valley
• Rohtang Pass
• Hadimba Temple

Food Recommendations
• Momos
• Trout Fish
• Himachali Thali

Cost Assessment

Accommodation : Rs. 12500
Food          : Rs. 5000
Transportation: Rs. 5000
Total Cost    : Rs. 22500
```

---

## Knowledge Representation

The system represents domain knowledge using structured dictionaries.

Each destination stores:

* Travel categories
* Budget information
* Tourist attractions
* Food recommendations
* Activities
* Cost parameters

This enables efficient retrieval and reasoning for recommendation generation.

---

## Test Cases Implemented

### Interest-Based Recommendation Tests

* Beach interest recommends Goa
* Adventure interest recommends Manali or Ladakh
* History interest recommends Jaipur
* Nature interest recommends Kerala or Manali

### Budget Validation Tests

* Low-budget users receive affordable recommendations
* Medium-budget users receive medium-range destinations
* High-budget users can access all destination categories

### Cost Assessment Tests

* Correct accommodation calculation
* Correct food cost calculation
* Correct transportation cost inclusion
* Correct total budget estimation

### Personalized Plan Tests

* Day-wise itinerary generation
* Activity assignment for all travel days
* Attraction display validation
* Food recommendation validation

### AI Recommendation Tests

* Interest matching verification
* Budget matching verification
* Destination ranking validation
* Recommendation consistency checks

---

## Performance Analysis

The travel planner performs recommendation generation using a lightweight scoring mechanism.

Metrics considered:

| Metric           | Description                     |
| ---------------- | ------------------------------- |
| Interest Score   | Measures preference matching    |
| Budget Score     | Measures affordability matching |
| Destination Rank | Final recommendation priority   |
| Estimated Cost   | Total trip expenditure          |

This approach provides fast and personalized recommendations while maintaining simplicity and scalability.

---

## Project Structure

```text
Q2-AITravelPlanner/
├── travel_planner.py
└── README.md
```

---

## Author

Sushanth Lingala
Roll No: **SE24UCSE168**
Course: **CS-2201 – Artificial Intelligence**
