<h1>Private-Tech-Market-Intelligence</h1>

## Overview
This project analyzes 100+ of the world's most valuable private technology companies through an interactive Tableau dashboard. The dashboard provides insights into valuation trends, funding efficiency, sector performance, and growth metrics in the private tech market.

## Problem Statement
Analyzing private tech companies requires gathering data from <a href = "https://finance.yahoo.com/markets/private-companies/highest-valuation/" > this website </a>. Later we utilized the scraped data to compare metrics across companies and sectors. This project solves that by creating a centralized platform for tracking and comparing private tech companies.

## Interactive <a href = "https://public.tableau.com/app/profile/mahmudul.hasan.nihan/viz/PrivateTechMarketIntelligenceDashboard/Dashboard1?publish=yes"> Dashboard</a> Components
  1. Market Overview Treemap: Visualizes sector dominance and valuation distribution
  2. Growth Performance Leaderboard: Ranks companies by 52-week growth
  3. Funding Efficiency Matrix: Quadrant analysis showing capital efficiency
  4. Sector Comparison Charts: Compares sectors across multiple metrics
  5. Company Size Distribution: Detailed views of individual companies
  
  You can visit the public dashboard <a href = "https://public.tableau.com/app/profile/mahmudul.hasan.nihan/viz/PrivateTechMarketIntelligenceDashboard/Dashboard1?publish=yes"> here </a>.


# Key Insights
## Market Structure
 <b>AI Dominance : </b> Artificial Intelligence sector leads in both valuation and funding

<b>Market Concentration : </b> Top 10 companies account for 70% of total valuation

<b>Sector Diversity : </b> 15+ different sectors represented with varying growth rates

## Performance Patterns
<b>Growth Leaders : </b> Companies like Ripple (+410%) and Anthropic (+231%) show exceptional growth

<b>Funding Efficiency : </b> Some companies achieve high valuations with relatively low funding

<b>Sector Trends : </b> Emerging sectors like Space Tech and Quantum Computing show early promise

## Build From Sources and Run the file
1. Clone the repo
``` bash
git clone https://github.com/Nihanhasan/Private-Tech-Market-Intelligence.git
```
2. Intialize and activate virtual environment
``` bash
virtualenv --no-site-packages  venv
source venv/bin/activate
```
3. Download Chrome WebDrive from https://chromedriver.chromium.org/downloads
4. Run the scraping program
```bash
python Private_tech_company_data.py --chromedriver_path <path_to_chromedriver>
```
5. You will get a file named Private_Companies_valuation_data.csv containing all the required fields. Alternatively, check our scraped data here: https://github.com/Nihanhasan/Private-Tech-Market-Intelligence/blob/main/Private_Companies_valuation_data.csv


##  License
This project is licensed under the MIT License - see the <a href = "https://github.com/Nihanhasan/Private-Tech-Market-Intelligence/blob/main/LICENSE"> LICENSE </a> file for details.

## Author
Mahmudul Hasan Nihan

<li>LinkedIn: https://www.linkedin.com/in/nihan-hasan/</li>

<li>GitHub: https://github.com/Nihanhasan</li>

<li>Email: mdnihan97@gmail.com</li>


## Acknowledgments
<li>Data provided by Yahoo Finance</li>
<li>Tableau Community for visualization inspiration</li>
<li>Open source contributors for tools and libraries</li>
<li>Mentors and peers for feedback and guidance</li>

#

<div align="center">
⭐ If you find this project useful, please give it a star on GitHub!
"Good decisions come from experience. Experience comes from making bad decisions. Data helps you make fewer bad decisions."

</div>













