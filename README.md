# Green-Tech Inventory Assistant (CLI)

## Candidate Name:
Ajinkya Deshpande

## Scenario Chosen:
Green-Tech Inventory Assistant

## Estimated Time Spent:
5-6 hours

## Quick Start:

### Prerequisites:
- Python 3.10+ (3.13 recommended)
- pip package manager
- Google Gemini API key (free tier available)
- `.env` file with configuration

### Installation:
```bash
pip install google-genai python-dotenv
```

### Configuration:
Create a `.env` file in the project root:
```
GEMINI_API_KEY=your_gemini_api_key_here
USE_AI=true
```

### Run:
```bash
python main.py
```

Load the data from JSON. 

We can also select data format:
- Option 1: Load from JSON
- Option 2: Load from CSV

But for now we are sticking to JSON, the data operations are done in CSV as well!

### Dashboard:
```bash
# View items with depletion analysis
1 -> View Item(s)

# Add Item to the database
2 -> Add Item

# Modify Item in the database
3 -> Modify Item

# Delete Item from the database
4 -> Delete Item

# Add Usage for the day
5 -> Add Usage Entry

# Make predictions for specific item
6 -> Predict depletion/wastage (asks for item name, validates, provides prediction with fallback)

# Get eco-friendly suggestions
7 -> Suggest other options

# View waste report with AI insights
8 -> Waste Report (shows metrics + AI-enhanced recommendations)

# Save changes
9 -> Save/Commit Changes & Exit
```


## AI Disclosure:

### Did you use AI?
Yes. Used Claude AI and Google Gemini API for:
- Code architecture and pattern suggestions
- Function implementations
- API integration logic
- Error handling strategies

### How did you verify it?
1. **Manual testing** - Tested each feature end-to-end with sample data
2. **Code review** - Verified all AI suggestions made logical sense
3. **Fallback testing** - Simulated API failures to test fallback mechanisms
4. **Logic validation** - Cross-checked calculations against manual math
5. **Edge cases** - Tested with empty inventory, zero usage, missing fields

## Tradeoffs & Prioritization:

### Known Limitations:
-  Database persistence (kept CSV/JSON instead for simplicity)
-  Real-time notifications (would require daemon/scheduler)
-  Advanced visualization (kept text-based output and input no visual I/O)
-  Expiry logic is still redundant, same items can have different days to expiry
-  No bulk order tracking
-  Average base predictions for daily usage
-  Used Gemini-2.5-flash, and no other model

### What would be build next?
1. **Demand forecasting** - Use historical trends to predict future usage patterns
2. **Supplier integration** - Connect to real supplier APIs for live pricing
3. **Waste reduction alerts** - Proactive notifications before waste happens
4. **Bulk order handling** - Dedicated logic to adjust calculations after bulk purchases
5. **Robust Expiry logic** - Add expiry date insted of days to expiry for the item
6. **ML Base forecasting** - Use actual ML models to predict the future dailyuse


## Architecture Overview:

### Core Modules:
- **main.py** - CLI interface and user interactions
- **predictor.py** - AI predictions for item depletion and bulk analysis
- **sustainability.py** - Eco-friendly suggestions and supplier recommendations
- **metrics.py** - Waste calculations, risk scoring, restock suggestions
- **data_loader.py** - JSON/CSV data persistence
- **data_operations.py** - Add/modify/delete inventory items
- **fallback.py** - Non-AI calculations for when API unavailable

### Key Features:
- **View inventory** with bulk depletion analysis
- **Predict depletion** with AI or fallback
- **Waste Report** with AI-enhanced recommendations
- **Sustainability suggestions** for eco-friendly alternatives
- **Restock recommendations** based on optimal quantity
- **Fallback mechanisms** when AI unavailable
- **Data persistence** in JSON/CSV formats

## Video Link for the detailed overview:

