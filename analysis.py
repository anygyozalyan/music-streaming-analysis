import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DATA_PATH = Path("data/viral_songs.csv")

df = pd.read_csv(DATA_PATH)

print(df.head())

print(df.shape)

print(df.columns.tolist())

# ==========================================
# DATA QUALITY CHECKS
# ==========================================

print(df.isnull().sum())

print(df.duplicated().sum())

print("Total track IDs:", len(df["track_id"]))
print("Unique track IDs:", df["track_id"].nunique())

print(df.dtypes)

print(df.describe())

# ==========================================
# STREAMS BY MUSIC GENRE
# ==========================================

genre_analysis = (
    df.groupby("genre").agg(
        track_count=("track_id", "count"),
        avg_streams=("streams", "mean"),
        median_streams=("streams", "median"),
        total_streams=("streams", "sum")
    )
    .sort_values("avg_streams", ascending=False)
)

print(genre_analysis.round(2).to_string())

# ==========================================
# VIRAL VS NON-VIRAL TRACKS
# ==========================================

viral_counts = df["viral"].value_counts().sort_index()
print(viral_counts)

viral_percentage = df["viral"].value_counts(
    normalize=True
).sort_index() * 100

print(viral_percentage.round(2))

viral_streams = df.groupby("viral").agg(
    track_count=("track_id", "count"),
    avg_streams=("streams", "mean"),
    median_streams=("streams", "median")
)

print(viral_streams.round(2).to_string())

viral_features = df.groupby("viral").agg(
    avg_danceability=("danceability", "mean"),
    avg_energy=("energy", "mean"),
    avg_valence=("valence", "mean"),
    avg_acousticness=("acousticness", "mean"),
    avg_instrumentalness=("instrumentalness", "mean")
)

print(viral_features.round(3).to_string())
    
# ==========================================
# CORRELATION ANALYSIS
# ==========================================

features = [
    "danceability",
    "energy",
    "valence",
    "acousticness",
    "instrumentalness",
    "streams"
]

correlation_matrix = df[features].corr()
print(correlation_matrix.round(2).to_string())

energy_correlation = df["energy"].corr(df["streams"])
print(round(energy_correlation, 3))

# ==========================================
# STEP 6: STREAMS BY RELEASE YEAR
# ==========================================

yearly_analysis = (
    df.groupby("release_year").agg(
        track_count=("track_id", "count"),
        avg_streams=("streams", "mean"),
        median_streams=("streams", "median")
    )
    .sort_index()
)

print(yearly_analysis.round(2).to_string())

# ==========================================
# TRACK CHARACTERISTICS AND STREAMS
# ==========================================

audio_features = [
    "danceability",
    "energy",
    "valence",
    "acousticness",
    "instrumentalness"
]

streams_correlations = (
    df[audio_features + ["streams"]]
    .corr()["streams"]
    .drop("streams")
    .sort_values(ascending=False)
)

print(streams_correlations.round(3).to_string())

# ==========================================
# VISUALIZATION
# Average Streams by Genre
# ==========================================

genre_plot = genre_analysis.sort_values(
    "avg_streams",
    ascending=True
)

plt.figure(figsize=(10, 6))

plt.barh(
    genre_plot.index,
    genre_plot["avg_streams"],
)

plt.title("Average Streams by Music Genre")
plt.xlabel("Average Number of Streams")
plt.ylabel("Music Genre")
plt.ticklabel_format(axis="x", style="plain")

plt.tight_layout()

plt.savefig(
    "charts/average_streams_by_genre.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# ==========================================
# VISUALIZATION 
# Viral vs Non-Viral Tracks
# ==========================================

viral_medians = df.groupby("viral")["streams"].median()

viral_medians.index = [
    "Non-viral (0)" if value == 0 else "Viral (1)"
    for value in viral_medians.index
]

plt.figure(figsize=(8, 5))

plt.bar(
    viral_medians.index,
    viral_medians.values
)

plt.title("Median Streams: Viral vs Non-Viral Tracks")
plt.xlabel("Track Status")
plt.ylabel("Median Number of Streams")
plt.ticklabel_format(axis="y", style="plain")

plt.tight_layout()

plt.savefig(
    "charts/median_streams_by_viral_status.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# ==========================================
# VISUALIZATION
# Viral Rate by Genre
# ==========================================

viral_rate = (
    df.groupby("genre")["viral"]
    .mean()
    .mul(100)
    .sort_values(ascending=True)
)

plt.figure(figsize=(10, 6))

plt.barh(
    viral_rate.index,
    viral_rate.values
)

plt.title("Percentage of Viral Tracks by Genre")
plt.xlabel("Viral Tracks (%)")
plt.ylabel("Music Genre")
plt.xlim(0, 100)

plt.tight_layout()


plt.savefig(
    "charts/viral_rate_by_genre.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# ==========================================
# VISUALIZATION 
# Average Streams by Release Year
# ==========================================
yearly_streams = (
    df.groupby("release_year")["streams"]
    .mean()
    .sort_index()
)
plt.figure(figsize=(10, 6))

plt.plot(
    yearly_streams.index,
    yearly_streams.values,
    marker="o"
)

plt.title("Average Streams by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Average Number of Streams")
plt.ticklabel_format(axis="y", style="plain")

plt.xticks(yearly_streams.index, rotation=45)

plt.tight_layout()

plt.savefig(
    "charts/average_streams_by_year.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
