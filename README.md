# European Hydrogen Projects Analysis

## Overview
This project analyzes hydrogen-related projects across Europe, focusing on project capacities, investments, and technological implementations. The analysis includes data processing, cleaning, and visualization of hydrogen production and infrastructure projects.

## Project Structure
```
honour/
├── README.md
├── graph.ipynb              # Main analysis notebook
├── country_list.csv         # Country reference data
├── df_cleaned.csv          # Intermediate cleaned dataset
├── europe_data.csv         # Final processed European dataset
```

## Key Features
- Data cleaning and preprocessing of hydrogen project data
- European country filtering and validation
- Technology categorization
- Temporal analysis (1992-2025)
- Investment and capacity analysis
- Regional distribution analysis

## Data Processing Pipeline
1. Initial data loading and validation
2. Country code standardization
3. European project filtering
4. Technology classification
5. Temporal range filtering (≤ 2025)
6. Missing value handling
7. Chronological ordering

## Dataset Features
- Project Name
- Country Information (ISO codes)
- Capacity (kt H2/y)
- Investment Costs (MUSD)
- Implementation Dates
- Technology Types
- Regional Classifications

## Requirements
- Python 3.x
- pandas
- plotly
- numpy

## Usage
1. Clone the repository
2. Install required dependencies:
```bash
pip install pandas plotly numpy
```
3. Run the Jupyter notebook:
```bash
jupyter notebook graph.ipynb
```

## Data Sources
- Primary project data
- Country classification data
- European regional mappings

## Contributing
Contributions are welcome. Please ensure your code follows the existing data processing pipeline structure.

## License
[MIT License or other appropriate license]

## Contact
[Your contact information]
