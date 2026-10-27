🎵 Music Streaming Analytics

What Drives Song Performance?

An exploratory data analysis project investigating the relationship between music characteristics, genres, viral status, and streaming performance.

The goal is to identify patterns in music streaming data, evaluate potential indicators of high-performing tracks, and translate analytical findings into actionable business insights.

⸻

📊 Project at a Glance

Project Detail	Description
Domain	Music Streaming Analytics
Dataset	10,000 tracks
Data Analysis	Exploratory Data Analysis (EDA)
Programming Language	Python
Libraries	pandas, Matplotlib
Key Methods	Data Quality Checks, Descriptive Statistics, Correlation Analysis, Data Visualization

⸻

🎯 Business Questions

This analysis explores five key questions:

1. Which music genres have the highest average streaming numbers?
2. How do viral and non-viral tracks differ?
3. Is energy associated with streaming performance?
4. How does streaming performance vary by release year?
5. Which audio characteristics are associated with streaming numbers?

⸻

🔍 Key Findings

1. Genre Performance

Latin tracks have the highest average streaming numbers in the dataset, followed by Hip-Hop and Electronic.

2. Viral vs. Non-Viral Tracks

Tracks labeled as viral have substantially higher streaming numbers than non-viral tracks. Their median streaming count is approximately 11.4 times higher.

3. Energy and Streaming Performance

The correlation between energy and streams is approximately 0.07, indicating a very weak positive linear relationship.

4. Audio Characteristics

Danceability shows a weak positive correlation with streams, while acousticness shows a weak negative correlation. These relationships alone are not sufficient to explain streaming performance.

5. Streaming Performance Over Time

Average and median streaming numbers fluctuate across release years, with no clear, consistent upward or downward trend.

⸻

📈 Visualizations

Charts generated using Python and Matplotlib.

Average Streams by Genre

Median Streams by Viral Status

Viral Rate by Genre

Average Streams by Release Year

⸻

💡 Business Implications

* Genre strategy: Investigate high-performing genres further when evaluating marketing opportunities.
* Content analysis: Explore combinations of audio characteristics rather than relying on a single feature.
* Performance measurement: Consider both average and median streams to avoid drawing conclusions from averages alone.
* Time-based comparisons: Account for the time tracks have had to accumulate streams.
* Further validation: Combine streaming data with additional information, such as playlist placements, marketing campaigns, and audience engagement, before making business decisions.

These are potential directions for further investigation, not proven causal recommendations.

⸻

🛠️ Tools & Skills

* Python
* pandas
* Matplotlib
* Exploratory Data Analysis (EDA)
* Data Quality Assessment
* Descriptive Statistics
* Correlation Analysis
* Data Visualization
* Business Insight Generation

⸻

📁 Project Structure

music-streaming-analysis/
├── data/
│   └── viral_songs.csv
├── charts/
│   ├── average_streams_by_genre.png
│   ├── median_streams_by_viral_status.png
│   ├── viral_rate_by_genre.png
│   └── average_streams_by_year.png
├── report/
│   └── analysis_report.md
├── analysis.py
└── README.md

⸻

⚠️ Limitations

* The criteria used to assign the viral label are not documented in the available dataset.
* Correlation does not establish causation.
* Streaming counts may be influenced by factors not included in the dataset.
* Tracks released more recently may have had less time to accumulate streams.

The findings should therefore be interpreted as patterns within this dataset rather than universal rules about music performance.

⸻

📄 Detailed Report

For the complete analysis, methodology, findings, and recommendations, see report/analysis_report.md.