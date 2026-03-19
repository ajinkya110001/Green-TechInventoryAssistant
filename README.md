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

Then select data format:
- Option 1: Load from JSON
- Option 2: Load from CSV

### Run Commands:
```bash
# View items with bulk depletion analysis
1 → View Item(s)

# Make predictions for specific item
5 → Predict depletion/wastage (asks for item name, validates, provides prediction with fallback)

# Get eco-friendly suggestions
6 → Suggest other options

# View waste report with AI insights
7 → Waste Report (shows metrics + AI-enhanced recommendations)

# Save changes
8 → Save & Commit Changes
```

### Test Commands:
```bash
# Test with sample data
python main.py
# Load existing data or create test items:
# - Add items with quantity and daily_usage
# - Add usage entries to build history
# - Run predictions/waste report to see AI analysis
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

### What did you cut?
-  Database persistence (kept CSV/JSON instead for simplicity)
-  Real-time notifications (would require daemon/scheduler)
-  Multi-user support (single-user CLI focused)
-  Advanced visualization (kept text-based output and input)
-  ML-based demand forecasting (used simple average for MVP)
-  Expiry logic is still redundant, same items can have different expiries

### What would be build next?
1. **Demand forecasting** - Use historical trends to predict future usage patterns
2. **Supplier integration** - Connect to real supplier APIs for live pricing
3. **Waste reduction alerts** - Proactive notifications before waste happens
4. **Bulk order handling** - Dedicated logic to adjust calculations after bulk purchases
5. **Robust Expiry logic** - 

### Known Limitations:
1. **No bulk order tracking** - System doesn't distinguish between normal orders and bulk orders; users must manually adjust quantities
2. **Average-based predictions** - Uses simple average of usage history; doesn't detect trends or seasonality
3. **Limited error handling** - Bare exception catches in some places
4. **Hardcoded model** - Uses gemini-2.5-flash; no configuration for other models

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
 **View inventory** with bulk depletion analysis
 **Predict depletion** with AI or fallback
 **Waste Report** with AI-enhanced recommendations
 **Sustainability suggestions** for eco-friendly alternatives
 **Restock recommendations** based on optimal quantity
 **Fallback mechanisms** when AI unavailable
 **Data persistence** in JSON/CSV formats
