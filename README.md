# parallel text Processing

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview
**text_miner** is a Python-based tool developed during an Infosys internship. This project focuses on extracting insights from large text files using sentiment analysis, text splitting, and ranking techniques. It's structured into modules to streamline tasks such as preprocessing, analysis, and aggregation of sentiment data. Perfect for learning or for building upon for text mining and NLP workflows.

## Features
- **Text Splitting**: Breaks down large text inputs into manageable chunks for analysis.
- **Sentiment Analysis**: Evaluates the emotional tone of each text segment.
- **Sentiment Ranking**: Orders text fragments based on sentiment strength or polarity.

## Project Structure

```
text_miner/
├── sentiment_analysis.py     # Performs sentiment analysis on text.
├── sentiment_ranking.py      # Orders text based on sentiment scores.
├── text_splitter.py          # Splits large text files into chunks.
├── splitter.py               # Possibly an auxiliary text splitter or variant.
├── utils/                    # Utility functions (helpers, text cleaning, etc.).
├── test/                     # Test scripts for validating module behavior.
├── huge.txt                  # Sample/large test input data.
└── LICENSE                   # MIT License.
```

## Getting Started

### Prerequisites
- **Python 3.8+**
- Recommended: Create and activate a virtual environment:
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  ```

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Garvithindoliya16/text_miner.git
   cd text_miner
   ```
2. (Optional) Install dependencies if there's a `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

## Usage Examples

Here are sample commands to run the scripts—adjust parameters as needed:

```bash
python text_splitter.py --input huge.txt --output chunks/
python sentiment_analysis.py --input chunks/ --output sentiment_results.csv
python sentiment_ranking.py --input sentiment_results.csv --top 10
```

*(Note: Please adjust flags/options to match what your scripts actually accept.)*

## How It Works
1. **Splitting** — `text_splitter.py` (or `splitter.py`) divides a large `.txt` file into smaller segments.
2. **Analyzing** — `sentiment_analysis.py` evaluates each segment to assign sentiment scores.
3. **Ranking** — `sentiment_ranking.py` organizes the segments by sentiment, enabling quick insights into the most emotionally charged pieces.

## Testing
To run tests:
```bash
pytest test/
```
Ensure all test files are present and properly structured in the `test/` directory.

## Contributing
Contributions, suggestions, and fixes are welcome!  
To contribute:
1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/YourFeature`.
3. Commit your changes: `git commit -m "Add: Some feature"`
4. Push to your branch: `git push origin feature/YourFeature`
5. Submit a Pull Request highlighting what you’ve improved or added.

## License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for full details.
