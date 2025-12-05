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


# Key Insights : Private Tech Market Dashboard
## Market Structure
   <li><b>Extreme concentration : </b> Top 5 companies =  65% of total valuation</li>
   <li><b>Long tail : </b> 100+ companies analyzed, but value clustered at top</li>
   <li><b>Valuation tiers : </b>2 Mega-cap (>$100B), 8 Large-cap, 37 Mid-cap, 53+ Small-cap</li>
   <li><b>Market Concentration : </b> Top 10 companies account for 70% of total valuation</li>
   <li><b>Sector Diversity : </b> 15+ different sectors represented with varying growth rates</li>

##  Sector Performance
   <li><b>AI dominates : </b>52% of total market value, +142% avg. growth </li>
   <li><b>Fastest growing : </b>Blockchain (+204%), AI (+142%), GovTech (+121%) </li>
   <li><b>Space Tech efficient : </b>High valuations with relatively lower funding </li>

## Capital Efficiency
   <li><b>Most efficient : </b>SpaceX ($60.90 valuation per $1 raised)</li>
   <li><b>AI variance : </b>OpenAI (10.2x ratio) vs. Scale AI (2.0x ratio)</li>
   <li><b>Funding doesn't guarantee value : </b>Some highly funded companies show lower efficiency ratios</li>

## Growth Leaders
   <li><b>Top performers : </b>Ripple (+410%), Anthropic (+231%), OpenAI (+153%)</li>
   <li><b>Sector trends : </b>100% of AI companies show positive growth</li>
   <li><b>Recovery signs : </b>Blockchain sector bouncing back strongly</li>

## Strategic Insights
   <li><b>AI sustainable : </b>Both largest and fastest-growing sector</li>
   <li><b>Efficiency matters : </b>High valuation-to-funding ratio correlates with strong fundamentals</li>
   <li><b>Funding evolution : </b>Tender offers increasing for mature private companies</li>
   <li><b>Sector rotation : </b>Money moving toward AI, Space, Blockchain</li>
   <li><b>Mid-cap momentum : </b>Strongest growth rates in $1-10B valuation range</li>

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













